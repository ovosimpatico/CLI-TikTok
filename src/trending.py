import sys

import atoma

import requests
from log import logtofile as log


def getInfoTrending():

    response = requests.get("https://proxitok.pabloferreiro.es/trending/rss")
    if response.status_code == 404:
        log(
            f"https://proxitok.pabloferreiro.es/trending/rss returned a 404 error. This is likely a server-side issue"
        )
        print(
            """Something went wrong while getting the trending information. 
This is likely an issue with your internet connection or with the API."""
        )
        sys.exit()
    if str(response.content) == "b''":
        print(
            "Something went wrong while parsing the trending information. If it persists, report this issue on Discord or Github."
        )
        log(
            "https://proxitok.pabloferreiro.es/trending/rss returned an empty response. This is likely a server-side issue"
        )
        sys.exit()
    return atoma.parse_rss_bytes(response.content)


def getLinksTrending():
    feed = getInfoTrending()
    linklist = []
    for i in feed.items:
        linklist.append(f"https://www.tiktok.com/" + i.link.split("/")[3] + "/video/" + i.link.split("/")[5])
    return linklist


def streamtrending():
    links = getLinksTrending()

    if len(links) == 0:
        print(
            "Something went wrong while parsing the trending information. If it persists, report this issue on Discord or Github."
        )
        log("The link list is empty. This is likely a server-side issue")
    from src.streaming import mpv

    for i in range(len(links)):
        mpv(links[i])
        log(f"{links[i]} was played")