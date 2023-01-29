import sys
from os import system


def init():
    # Intro for the user
    system("cls || clear")
    input(
        "Welcome to CLI TikTok, an open-source TikTok archiver and viewer!\nPress ENTER to proceed"
    )

    # Detect and install libraries - If they aren't installed,
    # the user is prompted to make the auto-installation.
    try:
        import atoma
        import requests
        import yt_dlp

        system("cls || clear")
    except ModuleNotFoundError:
        system("cls || clear")
        input(
            """
        The program detected dependencies are not installed
          Press ENTER to install the necessary libraries
          
     (You will need to open the program again afterwards)
              """
        )
        system("pip install -r requirements.txt --user")
        system("cls || clear")
        return -1

    # Search for updates, and prompts the user in case they're found.
    # If the user does not have internet access, warns him the software won't work properly and quit.
    try:
        import requests

        data = requests.get(
            "https://raw.githubusercontent.com/nanometer5088/CLI-TikTok/main/VERSION"
        )
        version = open("VERSION", "r", encoding="utf=8")
        if version.readline().rstrip() > (data.text):
            system("cls || clear")
            input(
                """
                      There's a new version available!
            Updates bring performance and feature improvements!
                    
                      Download the new version here: 
      https://github.com/nanometer5088/CLI-TikTok/archive/refs/heads/main.zip
                        
                        Press ENTER to proceed
                """
            )
        version.close()
    except requests.exceptions.ConnectionError:
        print(
            "CLI-TikTok detected your device isn't connected to the internet"
        )
        print(
            "This software requires a reliable and uncensored internet connection to properly work"
        )
        print("Please try again with an internet connection")
        sys.exit()
