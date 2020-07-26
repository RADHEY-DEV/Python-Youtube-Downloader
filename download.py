from pytube import YouTube

video_list = open("videosource.txt","r")


for i in video_list:
    yt = YouTube(i)

    try:

        dw = yt.streams.first()

        dw.download("./Downloads")

        print("Downloaded", i)

    except:
        print("Download failed for ", i)
