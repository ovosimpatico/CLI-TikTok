# Detect and handle launch with arguments

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--downloadliked", type=str)
parser.add_argument("--downloadcreator", type=str)

parser.add_argument("--streamlikedrandom", type=str)
parser.add_argument("--streamliked", type=str)

parser.add_argument("--streamcreator", type=str)
parser.add_argument("--streamtrending", type=str)

args = parser.parse_args()

from log import logtofile as log

import sys
# Introduction and pre-test
from src.init import init

silent = True
if len(sys.argv) <= 1:
    silent = False
    
a = init(silent)

if a == -1:
    print("Dependencies installed successfully.\nOpen the program again\n")
    log("Dependencies were installed, user was prompted to run the software again.")
    sys.exit()

log("Pre-test complete\n")


# Import libraries and required functions after sucessful pre-test
import os
import subprocess

from src.byuser import getLinks, streamuser
from src.downloader import downloadtiktoks
from src.functions import listas
from src.streaming import playback, playbackrandom
from src.trending import streamtrending

def main():
    # Needlessly big code to simply prompt the user which action they want to do
    log("Main menu started")
    try:
        question = int(
            input(
                """Do you want to download or watch tiktoks?
            
            (1) Download
            (2) Watch
            """
            )
        )
        os.system("cls || clear")

        ## Download
        if question == 1:
            downloadquestion = int(
                input(
                    """Do you want to download your liked videos or a creator?
            
            (1) Liked Videos
            (2) Creator
            """
                )
            )
            os.system("cls || clear")

            ## Download liked videos
            if downloadquestion == 1:
                log("The user chose to download liked videos\n")
                urls = listas()[0]
                downloadtiktoks(urls)
                sys.exit()

            ## Download creator
            if downloadquestion == 2:
                log("The user chose to download videos from a creator")
                print(
                    "Due to specific limitations of the current data method, downloading by creator will only get the latest 24 videos."
                )
                print(
                    "This limitation is being actively researched, any contributions will be welcome."
                )
                username = str(input("Enter the tiktok username here: "))
                log(f"The creator chosen was: @{username}\n")
                links = getLinks(username)
                downloadtiktoks(links)
                sys.exit()

        ## Stream
        if question == 2:

            watchquestion = int(
                input(
                    """Do you want to watch your liked videos, a creator or trending videos?
            
            (1) Liked Videos
            (2) Creator
            (3) Trending
            """
                )
            )
            os.system("cls || clear")

            ## Stream liked videos
            if watchquestion == 1:

                randomquestion = int(
                    input(
                        """Do you want to watch the tiktoks in randomized order?
                (1) Yes
                (2) No                                       
            """
                    )
                )
                os.system("cls || clear")

                ## Stream liked videos randomized
                if randomquestion == 1:
                    log("The user chose to stream liked videos in shuffled mode\n")
                    urls = listas()[0]
                    datas = listas()[1]
                    playbackrandom(urls, datas)
                    sys.exit()

                ## Stream liked videos in descending order
                if randomquestion == 2:
                    log("The user chose to stream liked videos in regular mode\n")
                    urls = listas()[0]
                    datas = listas()[1]
                    playback(urls, datas)
                    sys.exit()

            ## Stream creator
            if watchquestion == 2:
                log("The user chose to stream videos from a creator")
                print(
                    "Due to specific limitations of the current data method, watching by creator will only get the latest 24 videos."
                )
                print(
                    "This limitation is being actively researched, any contributions will be welcome."
                )
                username = str(input("Enter the tiktok username here: "))
                log(f"The creator chosen was: @{username}\n")
                streamuser(username)
                sys.exit()

            ## Stream trending videos
            if watchquestion == 3:
                log("The user chose to stream trending videos\n")
                print(
                    "Due to specific limitations of the current data method, watching by creator will only get the latest 24 videos."
                )
                print(
                    "This limitation is being actively researched, any contributions will be welcome."
                )
                streamtrending()
                sys.exit()

        # Error handling for invalid number (3, 4, 6, 133)
        log("The user entered an invalid numeric choice, and the software exited")
        print("The option you chose isn't valid.")

        # Error handling for invalid input (ENTER, 't', '5ga')
    except ValueError:
        log("The user entered an invalid non-numeric choice, and the software exited")
        print("The option you chose isn't valid.")

        # Error handling for missing user_data.json file
    except FileNotFoundError:
        log(
            "The user does not have a user_data.json file, but chose an option that depends on it, so the software exited"
        )
        print(
            "The 'user_data.json' file was not found. Make sure it is in the program folder and try again."
        )

        # Error handling for MPV media player or MPV not found in PATH
    except subprocess.CalledProcessError:
        log(
            "Tried to run MPV media player, but it was not found in the PATH, so the software exited"
        )
        os.system("cls || clear")
        print(
            "MPV media player was not found on your system path. Make sure it's installed and try again."
        )

        # Error handling for exiting the code with CTRL + C
    except KeyboardInterrupt:
        log("The user used CTRL + C to force-stop the software.")
        print("\n\tKeyboardInterrupt was detected - Goodbye!")


# Warning, this section is experimental and will only run if you use any launch arguments
# GUI Code:

def arguments(args):
    log("Running using launch arguments")

    if args.downloadliked:
        urls = listas()[0]
        downloadtiktoks(urls)

    elif args.downloadcreator:
        username = args.downloadcreator
        log(f"The creator chosen was: @{username}\n")
        links = getLinks(username)
        downloadtiktoks(links)

    elif args.streamlikedrandom:
        log("The user chose to stream liked videos in shuffled mode\n")
        urls = listas()[0]
        datas = listas()[1]
        playbackrandom(urls, datas)

    elif args.streamliked:
        log("The user chose to stream liked videos in regular mode\n")
        urls = listas()[0]
        datas = listas()[1]
        playback(urls, datas)

    elif args.streamcreator:
        log("The user chose to stream videos from a creator")
        print(
            "Due to specific limitations of the current data method, watching by creator will only get the latest 24 videos."
        )
        print(
            "This limitation is being actively researched, any contributions will be welcome."
        )
        username = args.streamcreator
        log(f"The creator chosen was: @{username}\n")
        streamuser(username)

    elif args.streamtrending:
        log("The user chose to stream trending videos\n")
        print(
            "Due to specific limitations of the current data method, watching by creator will only get the latest 24 videos."
        )
        print(
            "This limitation is being actively researched, any contributions will be welcome."
        )
        streamtrending()
        
if silent:
    arguments(args)
else:
    main()