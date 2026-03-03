import yt_dlp
import sys

# python -m pip install -U --pre "yt-dlp[default]"

# python download-mkv-youtube.py "https://www.youtube.com/watch?v=_2ELAjmcEc8"

youtube_url = sys.argv[1]

ydl_opts = { "outtmpl": "videos/%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" }

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
  ydl.download([youtube_url])
