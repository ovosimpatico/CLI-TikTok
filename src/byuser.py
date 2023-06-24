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
    from src.constants import OPTIONS
    log("Scraper started")
    print("\nObtaining URLs - this can take a while with users with many posts.")
    session = requests.Session()
    direct_links = []
    next_href = ""
    while True:
        url = f"{OPTIONS['proxitok_instance']}/@{username}{next_href}"
        response = session.get(url)
        log(f"Scraping {url}")
        
        if OPTIONS["ratelimit"] != 0:
            log(f'Sleeping for {OPTIONS["ratelimit"]}s')
            time.sleep(OPTIONS["ratelimit"])

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
