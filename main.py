from pytube import YouTube
from pytube import Playlist


path = r"C:\Users\uig62727\Desktop\Downloader\Muzica"
print("One audio file = 1, playlist = 2")
option = int(input())
int(option)

if option == 1:
    print("Video url: ")
    url_video = input()

    yt = YouTube(url_video)

    for i in yt.streams.filter(only_audio=True):

        print(i)

    itag = input()

    stream = yt.streams.get_by_itag(itag)
    stream.download(path)

if option==2:
    i = 1
    print("Playlist url: ")
    name = input()
    p = Playlist(name)
    s = 0
    for vid in p.videos:
        s+=1


    for vid in p.videos:
        audio = vid.streams.get_by_itag(251)
        audio.download(path)
        print("Downloaded " + str(i) + "/"+str(s))
        i+=1
        