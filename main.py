from src.functions import listas

from src.streaming import playbackrandom, playback

from src.downloader import downloadtiktoks

import configparser
configParser = configparser.RawConfigParser()
configFilePath = r'config.cfg'
configParser.read(configFilePath)

random = str(configParser.get('DEFAULT', 'random'))
downloader = str(configParser.get('DEFAULT', 'downloader'))

urls = listas()[0]
datas = listas()[1]

try:
    if downloader == 'True':
        downloadtiktoks(urls, datas)
    if downloader == 'False':
        if random == "True":
            playbackrandom(urls, datas)
        if random == "False":
            playback(urls, datas)
        else:
            print("Something went wrong with your configuration")
except KeyboardInterrupt:
    print("KeyboardInterrupt was detected.\nGoodbye!")