"""
StoryOps structured logger.

Writes two outputs per job:
  generated/logs/{job_id}.log    — human-readable, timestamped lines
  generated/logs/{job_id}.jsonl  — machine-readable JSONL for tooling

Each log entry carries: timestamp, level, job_id, pipeline stage, step counter,
message, and optional structured data dict. This lets you grep the log file for
plain reading, or parse the JSONL for metrics and dashboards.
"""

from __future__ import annotations

import json
import logging
import datetime as dt
from pathlib import Path
from typing import Any, Optional


class PipelineStage:
    ORCHESTRATE = "orchestrate"
    PLAN        = "plan"
    ASSEMBLE    = "assemble"
    WEAVE       = "weave"
    EXPORT      = "export"
    VERSION     = "version"
    REPORT      = "report"
    QUEUE       = "queue"


class StoryLogger:
    """
    Per-job structured logger.

    Usage:
        log = StoryLogger("gen_book01_ch001_v1")
        log.set_stage(PipelineStage.PLAN)
        log.info("Outline started", {"chapter_id": "ch001", "scene_count": 3})
        log.llm_call(PipelineStage.PLAN, "claude-3-5-sonnet", 4200, 180)
        log.llm_response("anthropic", "claude-3-5-sonnet", 3100, ["beats", "pacing_notes"])
        log.pipeline_complete("generated/drafts/ch001/v001.md", 1, 42.3)
    """

    def __init__(self, job_id: str, log_dir: Path = Path("generated/logs")):
        self.job_id = job_id
        self.log_dir = log_dir
        self.log_dir.mkdir(parents=True, exist_ok=True)

        self._stage: str = "init"
        self._step: int = 0
        self._start: float = _monotonic()

        self._log_path  = log_dir / f"{job_id}.log"
        self._json_path = log_dir / f"{job_id}.jsonl"

        # Python stdlib logger for console output
        self._logger = logging.getLogger(f"storyops.{job_id}")
        if not self._logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(
                logging.Formatter("[%(asctime)s] %(levelname)-5s %(name)s | %(message)s",
                                  datefmt="%H:%M:%S")
            )
            self._logger.addHandler(handler)
            self._logger.setLevel(logging.DEBUG)

    # ── Stage management ─────────────────────────────────────

    def set_stage(self, stage: str) -> None:
        self._stage = stage
        self._step = 0
        self._write("INFO", f"{'─'*20} STAGE: {stage.upper()} {'─'*20}")

    # ── Core write methods ───────────────────────────────────

    def info(self, message: str, data: Optional[dict] = None) -> None:
        self._write("INFO", message, data)

    def warn(self, message: str, data: Optional[dict] = None) -> None:
        self._write("WARN", message, data)

    def error(self, message: str, data: Optional[dict] = None) -> None:
        self._write("ERROR", message, data)

    def debug(self, message: str, data: Optional[dict] = None) -> None:
        self._write("DEBUG", message, data)

    # ── Semantic helpers (appear in JSONL with typed `event` field) ──

    def llm_call(self, stage: str, model: str, prompt_chars: int, system_chars: int) -> None:
        self._write("INFO", f"LLM call → {model} [{stage}]", {
            "event":        "llm_call",
            "stage":        stage,
            "model":        model,
            "prompt_chars": prompt_chars,
            "system_chars": system_chars,
        })

    def llm_response(
        self, provider: str, model: str, response_chars: int, parsed_keys: list[str]
    ) -> None:
        self._write("INFO", f"LLM response ← {provider}/{model} ({response_chars:,} chars)", {
            "event":          "llm_response",
            "provider":       provider,
            "model":          model,
            "response_chars": response_chars,
            "parsed_keys":    parsed_keys,
        })

    def scene_assembled(self, scene_id: str, knowledge_docs: int, source_chars: int) -> None:
        self._write("INFO", f"Scene assembled: {scene_id} ({knowledge_docs} knowledge docs)", {
            "event":          "scene_assembled",
            "scene_id":       scene_id,
            "knowledge_docs": knowledge_docs,
            "source_chars":   source_chars,
        })

    def continuity_flag(self, flag: str) -> None:
        self._write("WARN", f"Continuity flag: {flag}", {
            "event": "continuity_flag",
            "flag":  flag,
        })

    def missing_knowledge(self, docs: list[str]) -> None:
        self._write("WARN", f"LLM requested {len(docs)} missing knowledge doc(s)", {
            "event": "missing_knowledge",
            "docs":  docs,
        })

    def version_saved(self, version_num: int, file_path: str, pass_type: str, word_count: int) -> None:
        self._write("INFO", f"Version v{version_num:03d} saved → {file_path}", {
            "event":       "version_saved",
            "version_num": version_num,
            "file_path":   file_path,
            "pass_type":   pass_type,
            "word_count":  word_count,
        })

    def pipeline_complete(self, output_file: str, version: int, duration_secs: float) -> None:
        self._write("INFO", f"✓ Pipeline complete in {duration_secs:.1f}s → v{version:03d}", {
            "event":         "pipeline_complete",
            "output_file":   output_file,
            "version":       version,
            "duration_secs": round(duration_secs, 2),
        })

    def pipeline_skipped(self, reason: str) -> None:
        self._write("INFO", f"Pipeline skipped: {reason}", {
            "event":  "pipeline_skipped",
            "reason": reason,
        })

    def pipeline_error(self, error: str, exc: Optional[Exception] = None) -> None:
        detail = {"event": "pipeline_error", "error": error}
        if exc:
            detail["exception_type"] = type(exc).__name__
            detail["exception_msg"] = str(exc)
        self._write("ERROR", f"✗ Pipeline error: {error}", detail)

    # ── Internal ─────────────────────────────────────────────

    def _write(self, level: str, message: str, data: Optional[dict] = None) -> None:
        timestamp = dt.datetime.now(dt.timezone.utc).isoformat()
        elapsed   = round(_monotonic() - self._start, 2)
        self._step += 1

        # Human-readable line
        data_suffix = f"  {json.dumps(data)}" if data else ""
        human_line  = (
            f"[{timestamp}] [{level:<5}] [{self._stage:<12}] "
            f"[step={self._step:>3}] [+{elapsed:>6.1f}s] {message}{data_suffix}"
        )
        with self._log_path.open("a", encoding="utf-8") as fh:
            fh.write(human_line + "\n")

        # Structured JSONL
        record: dict[str, Any] = {
            "ts":      timestamp,
            "elapsed": elapsed,
            "level":   level,
            "job_id":  self.job_id,
            "stage":   self._stage,
            "step":    self._step,
            "msg":     message,
        }
        if data:
            record["data"] = data
        with self._json_path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(record) + "\n")

        # Console (INFO+ only for cleanliness)
        if level in ("INFO", "WARN", "ERROR"):
            console_msg = f"[{self._stage}] {message}"
            if level == "WARN":
                self._logger.warning(console_msg)
            elif level == "ERROR":
                self._logger.error(console_msg)
            else:
                self._logger.info(console_msg)


def _monotonic() -> float:
    import time
    return time.monotonic()
