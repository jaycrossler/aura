from __future__ import annotations

import argparse
import datetime as dt
import subprocess
import sys
import time
from pathlib import Path


def run(cmd: list[str], cwd: str = ".") -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd, check=False, capture_output=True, text=True)


def as_bool(raw: str) -> bool:
    return str(raw).strip().lower() in {"1", "true", "yes", "y", "on"}


def append_log(path: Path, line: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now(dt.timezone.utc).isoformat()
    with path.open("a", encoding="utf-8") as handle:
        handle.write(f"[{stamp}] {line}\n")


def changed(repo: str, remote: str, branch: str, log_file: Path) -> bool:
    fetch = run(["git", "fetch", remote, branch], cwd=repo)
    if fetch.returncode != 0:
        append_log(log_file, f"WARN fetch failed: {fetch.stderr.strip() or fetch.stdout.strip()}")
        return False

    local = run(["git", "rev-parse", "HEAD"], cwd=repo)
    remote_ref = run(["git", "rev-parse", f"{remote}/{branch}"], cwd=repo)
    if local.returncode != 0 or remote_ref.returncode != 0:
        append_log(log_file, "WARN unable to read local or remote refs")
        return False
    return local.stdout.strip() != remote_ref.stdout.strip()


def run_step(repo: str, log_file: Path, label: str, cmd: list[str]) -> bool:
    append_log(log_file, f"START {label}: {' '.join(cmd)}")
    result = run(cmd, cwd=repo)
    append_log(log_file, f"END {label}: exit={result.returncode}")
    if result.stdout.strip():
        append_log(log_file, f"STDOUT {label}:\n{result.stdout.strip()}")
    if result.stderr.strip():
        append_log(log_file, f"STDERR {label}:\n{result.stderr.strip()}")
    return result.returncode == 0


def process(repo: str, remote: str, branch: str, profile: str, run_generate: bool, run_agents: bool, log_file: Path) -> int:
    if not changed(repo, remote, branch, log_file):
        append_log(log_file, "No remote changes detected or remote unavailable.")
        return 0

    if not run_step(repo, log_file, "pull", ["git", "pull", "--ff-only", remote, branch]):
        return 2

    steps = [
        ("observe", [sys.executable, "-m", "tools.storyops.observe"]),
        ("lint", [sys.executable, "-m", "tools.storyops.lint", "--profile", profile]),
    ]
    if run_generate:
        steps.append(("generate", [sys.executable, "-m", "tools.storyops.generate"]))
    if run_agents:
        steps.append(("agents", [sys.executable, "-m", "tools.storyops.agents"]))
    steps.append(("publish", [sys.executable, "-m", "tools.storyops.publish"]))

    failures = 0
    for label, cmd in steps:
        if not run_step(repo, log_file, label, cmd):
            failures += 1
    append_log(log_file, f"Run completed with failures={failures}")
    return 1 if failures else 0


def main() -> None:
    parser = argparse.ArgumentParser(description="StoryOps polling service")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--remote", default="origin")
    parser.add_argument("--branch", default="main")
    parser.add_argument("--once", action="store_true")
    parser.add_argument("--interval-seconds", type=int, default=60)
    parser.add_argument("--profile", default="hard_scifi_novel")
    parser.add_argument("--run-generate", default="false")
    parser.add_argument("--run-agents", default="false")
    args = parser.parse_args()

    lock = Path(args.repo) / ".storyops.lock"
    log_file = Path(args.repo) / "generated/logs/local-runner.log"

    def loop() -> int:
        if lock.exists():
            append_log(log_file, "Skipped run because lock file exists.")
            return 3
        lock.write_text("locked", encoding="utf-8")
        try:
            return process(
                repo=args.repo,
                remote=args.remote,
                branch=args.branch,
                profile=args.profile,
                run_generate=as_bool(args.run_generate),
                run_agents=as_bool(args.run_agents),
                log_file=log_file,
            )
        finally:
            lock.unlink(missing_ok=True)

    if args.once:
        raise SystemExit(loop())

    while True:
        loop()
        time.sleep(max(5, args.interval_seconds))


if __name__ == "__main__":
    main()
