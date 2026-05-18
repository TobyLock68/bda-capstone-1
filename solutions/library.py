def download_video(url):
    from pathlib import Path
    import yt_dlp

    Path("videos").mkdir(exist_ok=True)
    ydl_options = {
        "outtmpl": "videos/%(title)s.%(ext)s",
        "socket_timeout": 30,
        "nocheckcertificate": True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_options) as ydl:
            ydl.download([url])
        return {
            "url": url, 
            "status": "success", 
            "error": ""
            }
    except Exception as e:
        return {
            "url": url, 
            "status": "failed", 
            "error": str(e)
            }
    

def read_video_urls(file_path):
    import csv
    urls = []

    with open(file_path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["title"], row["url"])
            urls.append(row["url"])
            
    return urls

def get_video_metadata(url):
    import yt_dlp

    ydl_options = {
        "quiet": True,
        "skip_download": True,
        "nocheckcertificate": True, #my issue with certificate means i need this
    }
    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        info = ydl.extract_info(url, download=False)
        return {
            "title": info.get("title"),
            "duration": info.get("duration"),
            "uploader": info.get("uploader"),
            "view_count": info.get("view_count"),
            "ext": info.get("ext"),
            "url": url,
        }
    
