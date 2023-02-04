import sys
from log import logtofile as log

import atoma
import requests


def getInfoTrending():

    response = requests.get("https://tik.hostux.net/trending/rss")
    if response.status_code == 404:
        log(f"https://tik.hostux.net/trending/rss returned a 404 error. This is likely a server-side issue")
        print("""Something went wrong while getting the trending information. 
This is likely an issue with your internet connection or with the API.""")
        sys.exit()
    if str(response.content) == "b''":
        print("Something went wrong while parsing the trending information. If it persists, report this issue on Discord or Github.")
        log("https://tik.hostux.net/trending/rss returned an empty response. This is likely a server-side issue")
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
        log("The link list is empty. This is likely a server-side issue")
    from src.streaming import mpv    
    for i in range(len(links)):

        mpv(links[i])
        log(f"{links[i]} was played")
