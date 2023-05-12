# import sys

import requests

from log import logtofile as log
from src.streaming import getVideoInfo, mpv

# import atoma


# def info(username):
#     rss_url = f"https://proxitok.pabloferreiro.es/@{username}/rss"
#     response = requests.get(rss_url)

#     if response.status_code == 404:
#         print("Something went wrong while getting the information. Make sure the username was correctly inserted and try again.")
#         log(f"{rss_url} returned a 404 error. The username is likely incorrect.")
#         sys.exit()

#     if not response.content:
#         print("The specified account does not exist.")
#         log(f"{rss_url} returned no information. The account likely does not exist.")
#         sys.exit()

#     return atoma.parse_rss_bytes(response.content)


# def getLinks(username):
#     feed = info(username)
#     links = []
#     for i in feed.items:
#         links.append(f"https://www.tiktok.com/@{username}/video/" + i.guid)
#     return links

def streamuser(username):
    links = proxitok_scraper(username)

    if not links:
        error_msg = "The link list is empty. The specified account is likely private or has no published videos"
        log(error_msg)
        print("This account is private or has no published videos.")
        return

    for link in links:
        url = getVideoInfo(link)
        mpv(url)
        log(f"Video {link} was played.")

import time

from bs4 import BeautifulSoup


def proxitok_scraper(username: str) -> list[str]:
    direct_links = []
    next_href = ""
    rate_limit = 0
    while True:
        url = f"https://proxitok.pussthecat.org/@{username}{next_href}"
        response = requests.get(url)

        if response.ok == False:
            if response.status_code == 404:
                print(f"@{username} does not exist or is banned.")
                return []
            elif response.status_code == 429 or response.status_code == 403:
                # may want to adjust this ratio
                rate_limit += 1
                sleep_time = 30 * rate_limit
                print(f"{response.status_code} {response.reason} sleeping for {sleep_time}")
                time.sleep(sleep_time)
                continue
            else:
                print(f"{response.status_code} {response.reason} getting {url}")
                return direct_links
            
        soup = BeautifulSoup(response.text, "html.parser")

        posts = soup.find_all("article", class_="media")
        
        if not posts:
            print(f"@{username} is private or has no videos.")
            return direct_links

        for post in posts:
            original_link = post.find("span", text="Original")

            if original_link:
                direct_links.append(original_link.parent.parent["href"])

        next_button = soup.find("a", class_="button", text="Next")
        if next_button.has_attr("disabled"):
            return direct_links
        else:
            next_href = next_button["href"]
            # stops rate limit from being hit on large accounts
            # can be removed if you want to only wait after you've been rate limited
            time.sleep(1)
