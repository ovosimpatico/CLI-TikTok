from src.functions import detect_dead_link
from src.functions import url_redirection

from yt_dlp import YoutubeDL

import os

def downloader(url):
    ydl_opts = {
    'ignoreerrors': True,
    'format': 'bestvideo*+bestaudio/best',
    'outtmpl': os.getcwd()+'/video/by-creator/%(creator)s/%(id)s.%(ext)s'
    }
    YoutubeDL(ydl_opts).download(url)
    
def downloadtiktoks(urls, datas):
    index = -1
    errorcount = []
    a = input(f"""
        **WARNING**
        This action will download up to {len(urls)} tiktoks in CLI-TIkTok/video/
        Ensure you have enough free space before proceeding!
        \nPress ENTER to proceed...
        """)
    if a != '':
        print('Operation canceled.')
        return
    while True:
        try:
            randomvideo = index = index + 1
            url = url_redirection(urls[randomvideo])
        
            if detect_dead_link(url) == True:
                print(f'\nVideo Liked - {datas[randomvideo]}\n')
                downloader(url)
            else:
                errorcount.append(urls)
        except IndexError:
            print("The tiktoks were downloaded")
            if len(errorcount) != 0:
                print(f'\n{len(errorcount)} video(s) failed to download.\nThe video(s) were likely banned or removed from the platform.')
                break
