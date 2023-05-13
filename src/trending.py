import time

import requests
from bs4 import BeautifulSoup

from log import logtofile as log


def streamtrending(amount:int = 24):
    links = proxitok_trending(amount)

    if len(links) == 0:
        print(
            "Something went wrong while parsing the trending information. If it persists, report this issue on Discord or Github."
        )
        log("The link list is empty. This is likely a server-side issue")
    from src.streaming import mpv

    for i in range(len(links)):
        mpv(links[i])
        log(f"{links[i]} was played")


def proxitok_trending(amount: int = 24) -> list[str]:
    from src.constants import APP
    log("Scraper started")
    print("\nObtaining URLs - this can take a while when requesting many posts.")
    session = requests.Session()
    direct_links = []
    next_href = ""
    rate_limit = 0
    while True:
        # The "next" page url is always the same but loads different trending videos each time
        url = f"{APP['proxitok_instance']}/trending{next_href}"
        # url = f"https://proxitok.pussthecat.org/trending{next_href}"
        response = session.get(url)
        log(f"Scraping {url}")
        
        if response.status_code == 429 or response.status_code == 403:
            # may want to adjust this ratio
            rate_limit += 1
            sleep_time = 30 * rate_limit
            print(f"{response.status_code} {response.reason} sleeping for {sleep_time}")
            log(f"\n{response.status_code} {response.reason} sleeping for {sleep_time}")
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
            error_msg = "No posts found for trending."
            log(error_msg)
            print(error_msg)
            return direct_links

        for post in posts:
            original_link = post.find("span", text="Original")

            if not original_link:
                continue

            direct_link = original_link.parent.parent["href"]
            # stops duplicate videos from being added to the list
            if not direct_link in direct_links:
                direct_links.append(direct_link)
                if len(direct_links) == amount:
                    return direct_links

        next_button = soup.find("a", class_="button", text="Next")
        next_href = next_button["href"]