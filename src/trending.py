import sys

import atoma
import requests


def getInfoTrending():

    response = requests.get("https://proxitok.pussthecat.org/trending/rss")
    if response.status_code == 404:
        print("""Something went wrong while getting the trending information. 
This is likely an issue with your internet connection or with the API.""")
        sys.exit()
    if str(response.content) == "b''":
        print("Something went wrong while parsing the trending information. If it persists, report this issue on Discord or Github.")
        sys.exit()
    return atoma.parse_rss_bytes(response.content)

def getLinksTrending():
    feed = getInfoTrending()
    linklist = []

    for i in range(len(feed.items)):
        linklist.append("https://www.tiktok.com" + feed.items[i].link)
    return linklist


def streamtrending():
    links = getLinksTrending()

    if len(links) == 0:
        print("Something went wrong while parsing the trending information. If it persists, report this issue on Discord or Github.")

    for i in range(len(links)):
        from src.streaming import mpv

        mpv(links[i])
