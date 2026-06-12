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
| 10| Zain Kahn          | LinkedIn, Twitter, Superhuman     | 2026-06-10             | Newsletter growth and email marketing tactics. |
## YouTube Transcript Script

I wrote a Python script (`get_youtube_transcripts.py`) to fetch transcripts from YouTube using the Supadata API. The script:

- Reads the API key from an environment variable (`SUPADATA_API_KEY`)
- Takes a list of YouTube video URLs
- Fetches the transcript in plain text for each video
- Saves each transcript as a Markdown file inside `research/youtube-transcripts/`
- Handles errors (videos without transcripts, API failures) gracefully
- Prints a summary of how many transcripts were saved

### How to run it
1. Set the API key: `$env:SUPADATA_API_KEY="your_key"`
2. Make sure the `supadata` package is installed: `pip install supadata`
3. Add your video URLs to the `youtube_urls` list inside the script
4. Run: `python get_youtube_transcripts.py`
5. Check the output in `research/youtube-transcripts/`