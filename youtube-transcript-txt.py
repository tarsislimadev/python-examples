from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse
import sys

# pip install youtube-transcript-api

# python youtube-transcript-txt.py "https://www.youtube.com/watch?v=FolDmUeaKng"

video_url = urlparse(sys.argv[1])
video_id = video_url.query.get("v")

language = "pt"

ytt_api = YouTubeTranscriptApi()
fetched_transcript = ytt_api.fetch(video_id, languages=[language])

with open(f"./{video_id}.{language}.txt", "w", encoding="utf-8") as f:
  for snippet in fetched_transcript:
    f.write(snippet.text + "\n")
