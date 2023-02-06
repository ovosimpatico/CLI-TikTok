import sys

import atoma

import requests
from log import logtofile as log
from src.streaming import getVideoInfo


def info(username):

    response = requests.get(f"https://tik.hostux.net/@{username}/rss")
    if response.status_code == 404:
        print(
            "Something went wrong while getting the information. Make sure the username was correctly inserted and try again."
        )
        log(
            f"https://tik.hostux.net/@{username}/rss returned a 404 error. The username is likely incorrect"
        )
        sys.exit()
    if str(response.content) == "b''":
        log(
            f"https://tik.hostux.net/@{username}/rss returned no information. The account likely does not exist"
        )
        print("The specified account does not exist.")
        sys.exit()

    # if response.description == None:
    #     log("This account does not have a bio.\n")
    # else:
    #     log(f"Bio: {str(response.description)}\n") ## TIKTOK BIO

    return atoma.parse_rss_bytes(response.content)


def getLinks(username):
    feed = info(username)
    linklist = []

    for i in range(len(feed.items)):
        linklist.append("https://www.tiktok.com" + feed.items[i].link)
    return linklist


def streamuser(username):
    links = getLinks(username)

    if len(links) == 0:
        log(
            "The link list is empty. The specified account is likely private or has no published videos"
        )
        print("This account is private or has no published videos.")
    from src.streaming import mpv, getVideoInfo

    for i in range(len(links)):
        url = getVideoInfo(links[i])
        mpv(url)
        log(f"Video {links[i]} was played.")
