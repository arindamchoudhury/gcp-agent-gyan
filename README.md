# Research Notes

A [Zensical](https://zensical.org/) static site built from personal notes on articles, docs, papers, and web sources.

## Run with Docker (recommended)

```powershell
docker compose up
# open http://localhost:8000
```

`zensical.toml` and `docs/` are bind-mounted — edits live-reload automatically.

## Run locally with Python

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install zensical livereload
python serve.py
```

## Fetch a new page for note-taking

The `scripts/fetch_page.py` script uses your installed Chrome to render JavaScript SPAs
and saves the text content to `cache/web/<slug>.txt`.

```powershell
& "C:\Users\arind\miniforge3\envs\notes-fetch\python.exe" scripts\fetch_page.py `
    "https://example.com/some-article" `
    --slug "my-article-slug"
# Saved to: cache/web/my-article-slug.txt
```

Options:
- `--slug`     Override the auto-generated cache file name
- `--out`      Override the cache directory (default: `cache/web`)
- `--timeout`  Page load timeout in ms (default: 30000; increase for slow SPAs)

## Add notes for a fetched page

After fetching, tell Claude Code:
> "Take notes on cache/web/my-article-slug.txt — source URL is https://..."
