import os

from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError

from log import logtofile as log
from src.functions import url_redirection


def downloader(url):
    ydl_opts = {
        "format": "bestvideo*+bestaudio/best",
        "outtmpl": os.getcwd() + "/video/%(creator)s/%(id)s.%(ext)s",
        "download_archive": os.getcwd() + "/video/.video_archive"
    }
    YoutubeDL(ydl_opts).download(url)


def downloadtiktoks(urls):
    index = -1
    errorcount = []
    a = input(
        f"""
        **WARNING**
        This action will download up to {len(urls)} tiktoks in CLI-TIkTok/video/
        Ensure you have enough free space before proceeding!
        \n\tPress ENTER to proceed...
        """
    )

    if a != "":
        log(f"User denied to download {len(urls)} tiktoks - Software exited")
        print("Operation canceled.")
        return
    log(f"User accepted to download {len(urls)} tiktoks")
    while True:
        try:
            randomvideo = index = index + 1
            url = url_redirection(urls[randomvideo])

            try:
                downloader(url)
                log(f"Video {url} was downloaded")
                print("")
            except DownloadError:
                print("This video is unavailable ")
                log(
                    f"Video {url} will not be downloaded - The video is unavailable (banned or taken down)"
                )
                errorcount.append(urls)

        except IndexError:
            print("The tiktoks were downloaded")
            log("The tiktoks were downloaded")
            if len(errorcount) != 0:
                print(
                    f"\n{len(errorcount)} video(s) failed to download.\nThe video(s) were likely banned or removed from the platform."
                )
                log(f"{len(errorcount)} video(s) failed to download.")
            return
