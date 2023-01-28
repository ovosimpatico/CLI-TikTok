# Introduction and pre-test
from src.init import init
import sys
a = init()
if a == -1:
    print("Dependencies installed successfully.\nOpen the program again\n")
    sys.exit()

# Import libraries and required functions after sucessful pre-test
from src.functions import listas
from src.streaming import playbackrandom, playback
from src.downloader import downloadtiktoks
from src.byuser import streamuser, getLinks
import os, subprocess

# Needlessly big code to simply prompt the user which action they want to do
try:
    question = int(input("""Do you want to download or watch tiktoks?
        
        (1) Download
        (2) Watch
        """))
    os.system("cls || clear")
    
    
    ## Download
    if question == 1:
        downloadquestion = int(input("""Do you want to download your liked videos or a creator?
        
        (1) Liked Videos
        (2) Creator
        """))
        os.system("cls || clear")
        
        ## Download liked videos
        if downloadquestion == 1:
            urls = listas()[0]
            downloadtiktoks(urls)
            sys.exit()
            
        ## Download creator
        if downloadquestion == 2:
            print('Due to specific limitations of the current data method, downloading by creator will only get the latest 30 videos.')
            print('This limitation is being actively researched, any contributions will be welcome.')
            username = str(input('Enter the tiktok username here: '))
            links = getLinks(username)
            downloadtiktoks(links)
            sys.exit()
        
    ## Stream
    if question == 2:
        
        watchquestion = int(input("""Do you want to watch your liked videos or a creator?
        
        (1) Liked Videos
        (2) Creator
        """))
        os.system("cls || clear")
        
        ## Stream liked videos
        if watchquestion == 1:
            
            
            randomquestion = int(input("""Do you want to watch the tiktoks in randomized order?
            (1) Yes
            (2) No                                       
        """))
            os.system("cls || clear")
            
            ## Stream liked videos randomized
            if randomquestion == 1:
                urls = listas()[0]
                datas = listas()[1]
                playbackrandom(urls, datas)
                sys.exit()
                
            ## Stream liked videos in descending order
            if randomquestion == 2:
                urls = listas()[0]
                datas = listas()[1]
                playback(urls, datas)
                sys.exit()
        
        ## Stream creator
        if watchquestion == 2:
            print('Due to specific limitations of the current data method, watching by creator will only get the latest 30 videos.')
            print('This limitation is being actively researched, any contributions will be welcome.')
            username = str(input('Enter the tiktok username here: '))
            streamuser(username)
            sys.exit()
            
    # Error handling for invalid number (3, 4, 6, 133)
    print("The option you chose isn't valid.")
    
    # Error handling for invalid input (ENTER, 't', '5ga')
except ValueError:
    print("The option you chose isn't valid.")
    
    # Error handling for missing Likes.txt file
except FileNotFoundError:
    print("The 'Likes.txt' file was not found. Make sure it is in the program folder and try again.")
    
    # Error handling for MPV media player or MPV not found in PATH
except subprocess.CalledProcessError:
    os.system("cls || clear")
    print("Mpv media player was not found on your system path. Make sure it's installed and try again.")
    
    # Error handling for exiting the code with CTRL + C
except KeyboardInterrupt:
    print("\n\tKeyboardInterrupt was detected - Goodbye!")