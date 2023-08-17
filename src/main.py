from pytube import YouTube

def download (url):
    youtube = YouTube(url)
    youtube = youtube.streams.get_highest_resolution()

    try:
        youtube.download(output_path = "/mnt/c/Users/peexp/Videos/youtube")
    except:
        print("An error has ocurred")
    
    print("Download is completed successfully")

url = input("Enter the YouTube video URL: ")
download(url)
