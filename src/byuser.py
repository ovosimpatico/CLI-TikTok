import sys

import atoma

import requests
from log import logtofile as log
from src.streaming import mpv, getVideoInfo

def info(username):
    rss_url = f"https://tik.hostux.net/@{username}/rss"
    response = requests.get(rss_url)

    if response.status_code == 404:
        print("Something went wrong while getting the information. Make sure the username was correctly inserted and try again.")
        log(f"{rss_url} returned a 404 error. The username is likely incorrect.")
        sys.exit()

    if not response.content:
        print("The specified account does not exist.")
        log(f"{rss_url} returned no information. The account likely does not exist.")
        sys.exit()

    return atoma.parse_rss_bytes(response.content)


def getLinks(username):
    feed = info(username)
    links = ["https://www.tiktok.com" + item.link for item in feed.items]
    return links

def streamuser(username):
    links = getLinks(username)

    if not links:
        error_msg = "The link list is empty. The specified account is likely private or has no published videos"
        log(error_msg)
        print("This account is private or has no published videos.")
        return

    for link in links:
        url = getVideoInfo(link)
        mpv(url)
        log(f"Video {link} was played.")
