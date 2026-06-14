# Portfolio Setup

## Tools Installed
- Cursor IDE
- Claude Code extension
- Codex extension
- Git (configured with user.name and user.email)
- Python + Supadata package


## Steps Completed (Phase 1)
1. Installed Cursor IDE from cursor.com
2. Added and logged into Claude Code extension
3. Added and logged into Codex extension
4. Created a public GitHub repository named `nuevo-repositorio`
5. Opened the repository in Cursor
6. Created this README.md file
7. Committed and pushed to GitHub


## Issues Encountered (Phase 1)
- Git wasn't configured with user.name and user.email, causing commit errors. Fixed by running `git config --global user.name` and `git config --global user.email`.
- Had to delete and recreate the repository because an auto-generated README on GitHub caused a push conflict.
- PowerShell required `.\` or `python` prefix to run the script (instead of just the filename).

---

# Research Project: Newsletter & Email Marketing for B2B SaaS

## Objective
Collect and organize insights from 10 leading practitioners in B2B SaaS email marketing and newsletters.


## Repository Structure
- `research/sources.md` — List of all 10 experts with links, notes, and why they were chosen.
- `research/youtube-transcripts/` — Transcripts of 1 YouTube video per expert, fetched via Supadata API.
- `research/linkedin-posts/` — 3 recent LinkedIn posts per expert about newsletters, email marketing, or B2B SaaS growth.
- `research/other/` — Additional materials (podcast notes, articles, etc.)
- `get_youtube_transcripts.py` — Python script that connects to the Supadata API and saves transcripts as Markdown files.


## Why These Experts?
I selected professionals who actively build, send, or advise on newsletters for B2B SaaS companies — not just theorists. Their content is practical, data-backed, and focused on growth and retention. Each expert has hands-on experience with email marketing for SaaS products, and their advice is tested in real campaigns.


## Current Status
- ✅ 10 experts identified and documented in `sources.md`
- ✅ YouTube transcripts collected for all 10 experts
- ✅ LinkedIn posts collected (3 posts per expert)


## How the Transcripts Were Obtained
1. Registered for a free Supadata API key at supadata.ai.
2. Installed the `supadata` Python package.
3. Wrote a script (`get_youtube_transcripts.py`) that takes a list of YouTube URLs and fetches each transcript.
4. Ran the script after setting the API key as an environment variable.
5. Transcripts were saved as `.md` files in `research/youtube-transcripts/`.

