from src.functions import detect_dead_link
from src.functions import url_redirection
from src.functions import listas

from src.streaming import getVideoInfo
from src.streaming import playback

import os

urls = listas()[0]
datas = listas()[1]

def main():
    while True:
        from src.functions import randomvideo
        
        os.system("cls || clear")
        randomvideo = randomvideo(urls)
        url = url_redirection(urls[randomvideo])
        
        if detect_dead_link(url) == True:
            print(f'\nVideo Liked - {datas[randomvideo]}\n')
            playback(url)

main()