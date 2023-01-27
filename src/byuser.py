import requests
import atoma
import sys

def by_user(username):

    response = requests.get(f'https://proxitok.pussthecat.org/@{username}/rss')
    if response.status_code == 404:
        print("Something went wrong while getting the information. Make sure the username was correctly inserted and try again.")
        sys.exit()
    if str(response.content) == "b''":
        print("The specified account does not exist.")
        sys.exit()
    feed = atoma.parse_rss_bytes(response.content)

    if feed.description == None:
        print("This account does not have a bio.")
    else:
        print(f'User: @{username}\nBio:\n')
        print(feed.description)
        print('')

    ### GET TIKTOK VIDEO
    try:
        for i in range(len(feed.items)):
            a = str(feed.items[i].link)

            link = 'https://www.tiktok.com'+a
        
            from src.streaming import mpv
            mpv(link)

    except IndexError:
        print("This account is private or has no published videos.")
