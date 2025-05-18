from pytube import YouTube

video_url = "https://youtu.be/LjjvIQzPDnI"

try:
    yt = YouTube(video_url)
    print(f"Title: {yt.title}")
    print(f"Channel: {yt.author}")
    print("Downloading...")

    stream = yt.streams.get_highest_resolution()
    stream.download()
    
    print("Download complete!")
except Exception as e:
    print("An error occurred:", e)