from pytube import YouTube
import os

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