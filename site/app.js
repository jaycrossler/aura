function fmt(n) {
  return new Intl.NumberFormat().format(n ?? 0);
}

function setList(id, items) {
  const el = document.getElementById(id);
  el.innerHTML = '';
  for (const item of items) {
    const li = document.createElement('li');
    if (item.href) {
      const a = document.createElement('a');
      a.href = item.href;
      a.textContent = item.label;
      a.target = '_blank';
      li.appendChild(a);
      if (item.extra) {
        li.append(` — ${item.extra}`);
      }
    } else {
      li.textContent = item.label;
    }
    el.appendChild(li);
  }
}

function wireRawToggle() {
  const btn = document.getElementById('toggle-raw');
  const pre = document.getElementById('content');
  btn.addEventListener('click', () => {
    const show = pre.hidden;
    pre.hidden = !show;
    btn.textContent = show ? 'Hide raw dashboard JSON' : 'Show raw dashboard JSON';
  });
}

function wireLintFilter(allItems) {
  const input = document.getElementById('lint-filter');
  input.addEventListener('input', () => {
    const q = input.value.trim().toLowerCase();
    const filtered = q
      ? allItems.filter((item) => item.label.toLowerCase().includes(q))
      : allItems;
    setList('lint-files', filtered);
  });
}

async function load() {
  wireRawToggle();
  for (const p of ['generated/site-data/dashboard.json', '../generated/site-data/dashboard.json']) {
    try {
      const r = await fetch(p);
      if (!r.ok) {
        continue;
      }
      const d = await r.json();
      document.getElementById('title').textContent = d.story_state?.project?.title || 'StoryOps Dashboard';
      document.getElementById('subtitle').textContent = `Updated ${d.story_state?.last_updated_utc || 'unknown time'}`;
      document.getElementById('summary').innerHTML = `
        <p><strong>Knowledge files:</strong> ${fmt(d.story_state?.summary?.knowledge_files)}</p>
        <p><strong>Total knowledge words:</strong> ${fmt(d.inventory_summary?.total_words)}</p>
        <p><strong>Lint findings:</strong> ${fmt(d.lint_findings_count)} (${JSON.stringify(d.lint_summary?.by_severity || {})})</p>
        <p><strong>Progress log entries:</strong> ${fmt(d.progress_log_entries)}</p>
      `;

      const lintItems = Object.entries(d.lint_by_file || {})
        .slice(0, 100)
        .map(([file, count]) => ({ label: `${file}: ${count}` }));
      setList('lint-files', lintItems);
      wireLintFilter(lintItems);

      const logs = Object.entries(d.log_paths || {}).map(([name, path]) => ({
        label: `${name} (${path})`,
        href: `../${path}`,
      }));
      setList('logs', logs);
      document.getElementById('content').textContent = JSON.stringify(d, null, 2);
      return;
    } catch (e) {
      // continue to fallback path
    }
  }
  document.getElementById('content').hidden = false;
  document.getElementById('content').textContent = 'Unable to load dashboard JSON.';
}

load();
