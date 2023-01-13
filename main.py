from src.functions import listas

from src.streaming import playbackrandom, playback

import configparser
configParser = configparser.RawConfigParser()
configFilePath = r'config.cfg'
configParser.read(configFilePath)
random = configParser.get('DEFAULT', 'random')


random = str(random)

urls = listas()[0]
datas = listas()[1]

try:
    if random == "True":
        playbackrandom(urls, datas)
    elif random == "False":
        playback(urls, datas)
    else:
        print("Something went wrong with your configuration")
except KeyboardInterrupt:
    print("KeyboardInterrupt was detected.\nGoodbye!")

print(random)
print(type(random))

