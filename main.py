# ===========================
# https://github.com/Drowys22
# Tysm for downloading this script!
# ===========================
import yt_dlp

url = input("please enter a url to download: ")

if url == "":
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
else:
    pass  

specs = {
    "format": "bestvideo+bestaudio/best",
    "outtmpl": "%(title)s.%(ext)s", }

with yt_dlp.YoutubeDL(specs) as f:
    f.download([url])
