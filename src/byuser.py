import time

import requests
from bs4 import BeautifulSoup

from log import logtofile as log
from src.streaming import getVideoInfo, mpv


def streamuser(username):
    links = proxitok_scraper(username)

    if not links:
        return

    for link in links:
        url = getVideoInfo(link)
        mpv(url)
        log(f"Video {link} was played.")


def proxitok_scraper(username: str) -> list[str]:
    print("\nObtaining URLs - this can take a while with users with many posts.")
    session = requests.Session()
    direct_links = []
    next_href = ""
    rate_limit = 0
    while True:
        url = f"https://proxitok.pussthecat.org/@{username}{next_href}"
        response = session.get(url)
        
        if response.status_code == 429 or response.status_code == 403:
            # may want to adjust this ratio
            rate_limit += 1
            sleep_time = 30 * rate_limit
            print(f"{response.status_code} {response.reason} sleeping for {sleep_time}")
            time.sleep(sleep_time)
            continue

        if not response.ok:
            error_msg = f"{response.status_code} {response.reason} getting {url}"
            log(error_msg)
            print(error_msg)
            return direct_links
            
        soup = BeautifulSoup(response.text, "html.parser")

        posts = soup.find_all("article", class_="media")
        
        if not posts:
            error_msg = "No posts found. The specified account is likely private or has no published videos"
            log(error_msg)
            print(f"@{username} is private or has no videos.")
            return direct_links

        for post in posts:
            original_link = post.find("span", text="Original")

            if not original_link:
                continue

            direct_links.append(original_link.parent.parent["href"])

        next_button = soup.find("a", class_="button", text="Next")
        if next_button.has_attr("disabled"):
            return direct_links
        next_href = next_button["href"]
