from src.functions import listas
from src.streaming import playbackrandom, playback
from src.downloader import downloadtiktoks
from src.byuser import by_user
import sys, os

urls = listas()[0]
datas = listas()[1]

try:
    question = int(input("""Welcome to CLI TikTok, an open-source TikTok viewer!
        
        Do you want to download or watch tiktoks?
        
        (1) Download
        (2) Watch
        """))
    os.system("cls || clear")
    ## DOWNLOAD
    if question == 1:
        downloadquestion = int(input("""Do you want to download your liked videos or a creator?
        
        (1) Liked Videos
        (2) Creator
        """))
        os.system("cls || clear")
        if downloadquestion == 1:
            downloadtiktoks(urls, datas)
            sys.exit()
        if downloadquestion == 2:
            print("Option still not implemented")
            sys.exit()
            # PLACEHOLDER UNTIL I DO CODE
        
    ## STREAM
    if question == 2:
        
        watchquestion = int(input("""Do you want to watch your liked videos or a creator?
        
        (1) Liked Videos
        (2) Creator
        """))
        os.system("cls || clear")
        if watchquestion == 1:
            
            #Liked videos random?
            randomquestion = int(input("""Do you want to watch the tiktoks in randomized order?
            (1) Yes
            (2) No                                       
        """))
            os.system("cls || clear")
            if randomquestion == 1:
                playbackrandom(urls, datas)
                sys.exit()
            if randomquestion == 2:
                playback(urls, datas)
                sys.exit()
        
        if watchquestion == 2:
            username = str(input('Enter the tiktok username here: '))
            by_user(username)
            sys.exit()
            
    print("The option you chose isn't valid.")
except ValueError:
    print("The option you chose isn't valid.")
except KeyboardInterrupt:
    print("\tKeyboardInterrupt was detected - Goodbye!")