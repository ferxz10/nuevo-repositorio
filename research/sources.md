# Expert Sources: Newsletter & Email Marketing for B2B SaaS

| # | Name               | Platforms                         | Recent Content | Notes |
|---|--------------------|-----------------------------------|------------------------|-------|
| 1 | Louis Grenier      | LinkedIn, Podcast, YouTube        | 2026-06-08             | Host of Everyone Hates Marketers; no‑fluff B2B marketing. |
| 2 | Val Geisler        | LinkedIn, Twitter                 | 2026-06-10             | Email strategist for SaaS; lifecycle and retention emails. |
| 3 | Dan Oshinsky       | LinkedIn, Inbox Collective        | 2026-06-10             | Consultant and operator of newsletters for SaaS. |
| 4 | Ann Handley        | LinkedIn, MarketingProfs, YouTube | 2026-06-05             | Content and email marketing thought leader. |
| 5 | Katelyn Bourgoin   | LinkedIn, Twitter, YouTube        | 2026-06-12             | Customer research and email marketing for SaaS. |
| 6 | Corey Haines       | LinkedIn, Swipe Files, The Juice  | 2026-06-11             | B2B SaaS marketing, newsletter growth strategies. |
| 7 | Dave Gerhardt      | LinkedIn, Exit Five Podcast       | 2026-06-12             | Ex‑VP Marketing at Drift, SaaS email & community. |
| 8 | Gaetano DiNardi    | LinkedIn, YouTube                 | 2026-05-28             | Growth advisor, SaaS email playbooks. |
| 9 | Ashley Guttuso     | LinkedIn, Twitter                 | 2026-04-12             | Email strategist for B2B SaaS; practical campaigns. |
| 10| Zain Kahn          | LinkedIn, Twitter, Superhuman     | 2026-06-10             | Newsletter growth and email marketing tactics. |## YouTube Transcript Script

We have created a Python script `get_youtube_transcripts.py` that fetches transcripts for YouTube videos using the Supadata API and saves them as Markdown files.

### Features:
- Reads the Supadata API key from the `SUPADATA_API_KEY` environment variable.
- Takes a list of YouTube video URLs (either defined in the script or read from a file).
- For each URL, extracts the transcript (plain text) and saves it as a Markdown file in `research/youtube-transcripts/`.
- The filename is derived from the video ID (or video title if available) and sanitized for filesystem safety.
- Includes error handling: skips videos without transcripts or on API failure, printing a warning.
- Prints a summary of successful transcripts at the end.

### Usage:
1. Set your Supadata API key as an environment variable:
   ```bash
   $env:SUPADATA_API_KEY="your_api_key_here"
   ```
2. Edit the script to add your YouTube video URLs to the `youtube_urls` list, or create a `youtube_urls.txt` file with one URL per line and uncomment the file reading section.
3. Run the script:
   ```bash
   python get_youtube_transcripts.py
   ```
4. Check the `research/youtube-transcripts/` directory for the generated Markdown transcripts.

### Notes:
- The script currently uses the video ID as the filename (since the Supadata transcript response does not include the video title). You can modify the script to fetch the video title via the YouTube API if desired.
- Ensure you have the `supadata` package installed (`pip install supadata`).
## YouTube Transcript Script

We have created a Python script `get_youtube_transcripts.py` that fetches transcripts for YouTube videos using the Supadata API and saves them as Markdown files.

### Features:
- Reads the Supadata API key from the `SUPADATA_API_KEY` environment variable.
- Takes a list of YouTube video URLs (either defined in the script or read from a file).
- For each URL, extracts the transcript (plain text) and saves it as a Markdown file in `research/youtube-transcripts/`.
- The filename is derived from the video ID (or video title if available) and sanitized for filesystem safety.
- Includes error handling: skips videos without transcripts or on API failure, printing a warning.
- Prints a summary of successful transcripts at the end.

### Usage:
1. Set your Supadata API key as an environment variable:
   ```bash
   $env:SUPADATA_API_KEY="your_api_key_here"
   ```
2. Edit the script to add your YouTube video URLs to the `youtube_urls` list, or create a `youtube_urls.txt` file with one URL per line and uncomment the file reading section.
3. Run the script:
   ```bash
   python get_youtube_transcripts.py
   ```
4. Check the `research/youtube-transcripts/` directory for the generated Markdown transcripts.

### Notes:
- The script currently uses the video ID as the filename (since the Supadata transcript response does not include the video title). You can modify the script to fetch the video title via the YouTube API if desired.
- Ensure you have the `supadata` package installed (`pip install supadata`).
