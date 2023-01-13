from yt_dlp import YoutubeDL

import subprocess


def getVideoInfo(url):
    ydl_opts = {
    "quiet":    True,
    "simulate": True,
    "forceurl": True
    }
    
    return YoutubeDL(ydl_opts).extract_info(url)["url"]

def playback(url):
    subprocess.check_output(f'mpv "{getVideoInfo(url)}"', shell=False)