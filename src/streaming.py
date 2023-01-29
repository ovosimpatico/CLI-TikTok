import os
import subprocess

from src.functions import detect_dead_link, url_redirection
from yt_dlp import YoutubeDL


def getVideoInfo(url):
    ydl_opts = {"quiet": True, "simulate": True, "forceurl": True}

    return YoutubeDL(ydl_opts).extract_info(url)["url"]


def mpv(url):
    subprocess.check_output(f'mpv "{getVideoInfo(url)}"', shell=True)


def playbackrandom(urls, datas):
    while True:
        os.system("cls || clear")
        from src.functions import randomvideo

        randomvideo = randomvideo(urls)
        url = url_redirection(urls[randomvideo])

        if detect_dead_link(url) == True:
            print(f"\nVideo Liked - {datas[randomvideo]}\n")
            mpv(url)


def playback(urls, datas):
    index = 0
    while True:
        os.system("cls || clear")
        try:
            randomvideo = index = index + 1
            url = url_redirection(urls[randomvideo])

            if detect_dead_link(url) == True:
                print(f"\nVideo Liked - {datas[randomvideo]}\n")
                mpv(url)
        except IndexError:
            print("All tiktoks were played.")
            break
