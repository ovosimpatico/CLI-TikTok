import sys
from os import system

from log import logtofile as log


def init():
    # Intro for the user
    system("cls || clear")
    input(
        "Welcome to CLI TikTok, an open-source TikTok archiver and viewer!\nPress ENTER to proceed"
    )

    # Detect and install libraries - If they aren't installed,
    # the user is prompted to make the automatic installation.
    log("Started dependency test")
    try:
        import atoma
        import requests
        import yt_dlp

        system("cls || clear")
        log("Dependency test sucessful!")
    except ModuleNotFoundError:
        log("Dependency test failed - Missing library")
        system("cls || clear")
        input(
            """
        The program detected dependencies are not installed
          Press ENTER to install the necessary libraries
          
     (You will need to open the program again afterwards)
              """
        )
        log("User accepted automatic installation, running it.")
        system("pip install -r requirements.txt --user")
        system("cls || clear")
        return -1

    # Search for updates, and prompts the user in case they're found.
    # If the user does not have internet access, warns him the software won't work properly and quit.
    try:
        import requests

        log("Started update / networking test")
        data = requests.get(
            "https://raw.githubusercontent.com/nanometer5088/CLI-TikTok/main/VERSION"
        )
        version = open("VERSION", "r", encoding="utf=8")
        userversion = version.readline().rstrip()
        if userversion < (data.text):
            log(
                f"New version detected! User version is {userversion}, but {data.text} was found on Github."
            )
            system("cls || clear")
            log("User was prompted to update")
            input(
                """
                      There's a new version available!
            Updates bring performance and feature improvements!
                    
                      Download the new version here: 
      https://github.com/nanometer5088/CLI-TikTok/archive/refs/heads/main.zip
                        
                        Press ENTER to proceed
                """
            )
            system("cls || clear")
        else:
            log("The user has internet acess and the software is up-to-date.")
        version.close()
    except requests.exceptions.ConnectionError:
        log(
            "A connection error was detected when trying to connect to https://raw.githubusercontent.com/ to check for updates."
        )
        print("CLI-TikTok detected your device isn't connected to the internet")
        print(
            "This software requires a reliable and uncensored internet connection to properly work"
        )
        print("Please try again with an internet connection")
        log("The software exited, and the user was notified of the connection problem.")
        sys.exit()
