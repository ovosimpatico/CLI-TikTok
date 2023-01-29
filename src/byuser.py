import sys

import atoma
import requests


def info(username):

    response = requests.get(f"https://proxitok.pussthecat.org/@{username}/rss")
    if response.status_code == 404:
        print(
            "Something went wrong while getting the information. Make sure the username was correctly inserted and try again."
        )
        sys.exit()
    if str(response.content) == "b''":
        print("The specified account does not exist.")
        sys.exit()
    return atoma.parse_rss_bytes(response.content)

    # if feed.description == None:
    #     print("This account does not have a bio.")
    # else:
    #     print(feed.description) ## TIKTOK BIO


def getLinks(username):
    feed = info(username)
    linklist = []

    for i in range(len(feed.items)):
        linklist.append("https://www.tiktok.com" + feed.items[i].link)
    return linklist


def streamuser(username):
    links = getLinks(username)

    if len(links) == 0:
        print("This account is private or has no published videos.")

    for i in range(len(links)):
        from src.streaming import mpv

        mpv(links[i])
