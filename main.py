from pytube import YouTube
from pytube import Playlist
import os

print("Audio only = 1, playlist = 2")
option = int(input())
int(option)

if option == 1:

    url_video = input()

    yt = YouTube(url_video)

    for i in yt.streams.filter(only_audio=True):

        print(i)

    itag = input()

    stream = yt.streams.get_by_itag(itag)
    stream.download(r'C:\Users\Adrian\Desktop\Muzica')

    os.chdir('C:/Users/Adrian/Desktop/Muzica')
    src = stream.title+'.webm'
    dest = stream.title+'.mp3'
    os.rename(src,dest)

if option==2:
    i = 1
    name = input()
    p = Playlist(name)
    s = 0
    for vid in p.videos:
        s+=1


    for vid in p.videos:
        audio = vid.streams.get_by_itag(251)
        audio.download(r'C:\Users\Adrian\Desktop\Muzica')
        print("Downloaded " + str(i) + "/"+str(s))
        i+=1
        os.chdir('C:/Users/Adrian/Desktop/Muzica')
        src = audio.title+'.webm'
        dest = audio.title+'.mp3'
        os.rename(src,dest)