import yt_dlp

def download_video(url, output_path='videos'):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

video_url = 'https://www.youtube.com/watch?v=n40_fosrDmw'
download_video(video_url)
