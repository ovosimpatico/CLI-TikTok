import os
import random

import requests
from log import logtofile as log

def listas():
    # Retrieves tiktok likes and dates from user_data.json
    import json
    f = open('user_data.json')
    linklist = []
    datelist = []
    data = json.load(f)

    for i in data['Activity']["Like List"]['ItemFavoriteList']:
        linklist.append(i['Link'])
        datelist.append(i['Date'])
    f.close()
    log("user_data.json file was processed sucessfully")
    return linklist, datelist


# Broken as of 2023-02-03
# A workaround has been put in place
def detect_dead_link(url):
    # Detects if the video is available to be streamed or downloaded.
    dead_url_start_with = "https://www.tiktok.com/@/video"
    # No user on the @ means video was removed, taken down or isn't in a video format
    if dead_url_start_with in url:
        return False  # Means do not proceed with the download
    else:
        return True  # Means it's all clear to download.


def url_redirection(url):
    # Tiktok links from the user_data.json are shortened. They need to be redirected to the final link, which is done here.
    headers = {
        # Chrome 113 on Windows 10 - Common useragent to reduce chances of a captcha
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    return response.url


def randomvideo(urls):
    # Chooses a random video from user_data.json - Optional Feature
    return random.randint(0, (len(urls) - 1))
