#!/usr/bin/env python3
"""
Script to fetch transcripts for YouTube videos using Supadata and save them as Markdown files.
"""

import os
import re
from supadata import Supadata, SupadataError

def sanitize_filename(title):
    """Convert a video title into a safe filename."""
    # Remove invalid characters for filenames
    title = re.sub(r'[<>:"/\\|?*\x00-\x1F]', '', title)
    # Replace spaces with hyphens and convert to lowercase
    title = re.sub(r'\s+', '-', title.strip()).lower()
    # Remove multiple hyphens
    title = re.sub(r'-+', '-', title)
    return title

def main():
    # Read API key from environment variable
    api_key = os.getenv('SUPADATA_API_KEY')
    if not api_key:
        print("Error: SUPADATA_API_KEY environment variable not set.")
        return 1

    # Initialize the client
    supadata = Supadata(api_key=api_key)

    youtube_urls = [
        "https://www.youtube.com/watch?v=cFeeFId_lzI",
        "https://www.youtube.com/watch?v=Z_3cTExgYMg",
        "https://www.youtube.com/watch?v=U0uCjo1tcZY",
        "https://www.youtube.com/watch?v=C5amYDbo8G0",
        "https://www.youtube.com/watch?v=jhjpY27-_uw",
        "https://www.youtube.com/watch?v=jC84O09_8ys",
        "https://www.youtube.com/watch?v=4YlgH4pRrI8",
        "https://www.youtube.com/watch?v=9INQVyJZeeI",
        "https://www.youtube.com/watch?v=0DS_HhV3WkE",
        "https://www.youtube.com/watch?v=3KAC5EwKuNw",
    ]


    # Create output directory
    output_dir = os.path.join('research', 'youtube-transcripts')
    os.makedirs(output_dir, exist_ok=True)

    success_count = 0
    for url in youtube_urls:
        try:
            
            video_id_match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11})', url)
            if not video_id_match:
                print(f"Warning: Could not extract video ID from URL: {url}")
                continue
            video_id = video_id_match.group(1)

            # Fetch transcript
            transcript_data = supadata.transcript(
                url=url,
                lang="en",
                text=True,
                mode="auto"
            )

            # If transcript_data is a string (because text=True), use it directly.
            # Otherwise, if it's a list of chunks, we join them.
            if isinstance(transcript_data, list):
                transcript_text = "\n\n".join([chunk.get('text', '') for chunk in transcript_data])
            else:
                transcript_text = transcript_data
            title = video_id  # fallback to video ID

            # Create a safe filename
            filename = f"{sanitize_filename(title)}.md"
            filepath = os.path.join(output_dir, filename)

            # Save transcript as Markdown
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"# Transcript for {title}\n\n")
                f.write(f"Source: {url}\n\n")
                f.write(transcript_text)

            print(f"Saved transcript for {title} to {filepath}")
            success_count += 1

        except SupadataError as e:
            print(f"Warning: Supadata error for URL {url}: {e}")
        except Exception as e:
            print(f"Warning: Unexpected error for URL {url}: {e}")

    print(f"\nSummary: Successfully saved {success_count} transcript(s) out of {len(youtube_urls)} URLs.")
    return 0

if __name__ == "__main__":
    exit(main())                                                                          
