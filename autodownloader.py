import urllib3
import wget 
import sys
import os
from pytube import YouTube
#from pathlib import Path
#from unipath import Path

print ("~"*50)
print ("             Auto Downloader")
print ("        Created by : Sayak Naskar")
print ("~"*50)
print ("1.Download text, pdf, html files .\n2.Download video from youtube .")
select = int(input("Enter Your choice :"))

if select == 1:
    url = input("Enter your URL to download mp3,pdf :")
    save_path = (input("Enter your path: "))
    print(wget.download(url))
    save = sys.path.append(save_path)
    #save = os.sys(save_path,down_file)
    #open(str(save), 'r')
   # print (file.read())
    with open(str(save)) as fileopen:
        read = fileopen.read()
        print(read)
    print ("Your file :"+wget.detect_filename(url=url))
elif select == 2:  
    url1 = input("Enter your URL to download your video :")
    YouTube(url1).streams.first().download()
    yt = YouTube(url1)
    yt.streams



