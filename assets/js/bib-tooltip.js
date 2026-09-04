 (function () {
    const buttons = document.querySelectorAll('.btn-bib');
    if (!buttons.length) return;

    function parseBib(text) {
      const entries = {};
      let i = 0;
      while (i < text.length) {
        if (text[i] !== '@') {
          i += 1;
          continue;
        }
        const start = i;
        const lbrace = text.indexOf('{', i);
        if (lbrace < 0) break;
        let depth = 1;
        let k = lbrace + 1;
        while (k < text.length && depth > 0) {
          const c = text[k];
          if (c === '{') depth += 1;
          else if (c === '}') depth -= 1;
          if (depth === 0) break;
          k += 1;
        }
        if (depth !== 0) break;
        const entry = text.substring(start, k + 1);
        const m = entry.match(/^@\w+\s*\{\s*([\w-]+)\s*,/);
        if (m) entries[m[1]] = entry;
        i = k + 1;
      }
      return entries;
    }

    fetch('/files/papers.bib')
      .then((r) => (r.ok ? r.text() : Promise.reject('bib fetch ' + r.status)))
      .then((text) => {
        const data = parseBib(text);
        const tip = document.createElement('div');
        tip.className = 'bib-tooltip';
        document.body.appendChild(tip);

        buttons.forEach((btn) => {
          const key = btn.dataset.bibKey;
          const entry = key && data[key];

          btn.addEventListener('click', (e) => {
            e.preventDefault();
            if (!entry) return;
            navigator.clipboard.writeText(entry).then(() => {
              const orig = btn.textContent;
              btn.textContent = 'Copied';
              setTimeout(() => {
                btn.textContent = orig;
              }, 2000);
            }).catch((err) => console.warn('[bib-tooltip] copy failed', err));
          });

          if (!entry) return;

          btn.addEventListener('mouseenter', () => {
            tip.textContent = entry;
            tip.style.display = 'block';
            const r = btn.getBoundingClientRect();
            tip.style.left = (r.left + window.scrollX) + 'px';
            tip.style.top = (r.bottom + window.scrollY + 6) + 'px';
          });
          btn.addEventListener('mouseleave', () => {
            tip.style.display = 'none';
          });
        });
      })
      .catch((err) => console.warn('[bib-tooltip]', err));
  })();
