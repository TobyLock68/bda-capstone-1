def download_video(url):
    # import ssl
    # import certifi
    # import os

    # # This force-points Python to use the certifi certificate bundle
    # ssl._create_default_https_context = ssl._create_unverified_context
    # # OR more accurately for your environment:
    # os.environ['SSL_CERT_FILE'] = certifi.where()

    from pathlib import Path
    import yt_dlp

    Path("videos").mkdir(exist_ok=True)


    ydl_options = {
    "outtmpl": "videos/%(title)s.%(ext)s"
    }

    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        ydl.download([url])


def read_video_urls(file_path):
    import csv
    urls = []

    with open(file_path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["title"], row["url"])
            urls.append(row["url"])
            
    return urls