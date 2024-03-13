from pytube import YouTube
from pytube import Playlist
from pathlib import Path


def progressBar(iteration, total):
    fill = '█'
    fill_fength = int(iteration*100//total)
    bar = fill*fill_fength + "_"*(100 - fill_fength)
    print(f'\r{bar}{fill_fength}% | 100%', end='\r')

    if iteration == total:
        print()

print("One audio file = 1, playlist = 2")
path = str(Path.cwd()) + "\Muzica"
option = int(input())
int(option)

if option == 1:
    print("Video url: ")
    url_video = input()
    yt = YouTube(url_video)

    for i in yt.streams.filter(only_audio=True):
        print(i)

    print("Intput itag(ex: 251): ")
    itag = input()
    stream = yt.streams.get_by_itag(itag)
    stream.download(path)

if option==2:
    i = 0
    print("Playlist url: ")
    name = input()
    p = Playlist(name)
    s = 0
    for vid in p.videos:
        s+=1

    for vid in p.videos:
        audio = vid.streams.get_by_itag(251)
        audio.download(path)
        i += 1
        progressBar(i,s)
        