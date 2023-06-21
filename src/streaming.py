import os
import subprocess

from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError

from log import logtofile as log
from src.functions import url_redirection
from src.constants import OPTIONS


def getVideoInfo(url):
    ydl_opts = {"quiet": True, "simulate": True, "forceurl": False}

    return YoutubeDL(ydl_opts).extract_info(url)["url"]


def mpv(url):
    subprocess.check_output(f'{OPTIONS["player_command"]} "{getVideoInfo(url)}"', shell=True)


def playbackrandom(urls, datas):
    while True:
        from src.functions import randomvideo

        os.system("cls || clear")

        randomvideo = randomvideo(urls)
        url = url_redirection(urls[randomvideo])

        try:
            link = getVideoInfo(url)
            print(f"\nVideo Liked - {datas[randomvideo]}\n")
            mpv(link)
            log(f"Video {url} was reproduced")
        except DownloadError:
            log(
                f"Video {url} could not be played, it might have been banned or taken down"
            )
            print("Video could not be played, it might have been banned or taken down.")


def playback(urls, datas):
    index = 0
    while True:
        os.system("cls || clear")
        try:
            randomvideo = index = index + 1
            url = url_redirection(urls[randomvideo])

            try:
                link = getVideoInfo(url)
                print(f"\nVideo Liked - {datas[randomvideo]}\n")
                mpv(link)
                log(f"Video {url} was reproduced")
            except DownloadError:
                log(
                    f"Video {url} could not be played, it might have been banned or taken down"
                )
                print(
                    "Video could not be played, it might have been banned or taken down."
                )
        except IndexError:
            log("All tiktoks were played")
            print("All tiktoks were played.")
            break
