import requests
import random
import os


def listas():
    #Retrieves tiktok links and dates from Likes.txt
    i = 0
    arquivo = open('Likes.txt', 'r', encoding='utf-8')
    linhas = arquivo.readlines()
    tamanho = len(linhas)
    arquivo.close()

    vet = []
    listalinks = []
    listadatas = []
    arquivo = open('Likes.txt', 'r', encoding='utf-8')

    while i <= tamanho:
        lelinha = arquivo.readline().rstrip()
        vet.append(lelinha.split())
        i += 1
    arquivo.close()

    for i in range(2, len(vet), 3):
        listalinks.append(vet[i-1][1])

    for i in range(2, len(vet), 3):
        listadatas.append(vet[i-2][1] + ' ' + vet[i-2][2])

    return listalinks, listadatas


#Unused function - Might be useful in future iterations of the project
#https://github.com/nanometer5088/CLI-TikTok/commit/ad589d7b324042ee85a270625df3ad9f6f82ab8a 
def removevideo():
    if os.path.exists(os.getcwd()+"/video/video"):
        os.remove(os.getcwd()+"/video/video")
    else:
        pass


def detect_dead_link(url):
    #Detects if the video is available to be streamed or downloaded.
    dead_url_start_with = 'https://www.tiktok.com/@/video' 
    #No user on the @ means video was removed, taken down or isn't in a video format
    if dead_url_start_with in url:
        return False # Means do not proceed with the download
    else:
        return True # Means it's all clear to download.
    

def url_redirection(url):
    #Tiktok links from the Likes.txt are shortened. They need to be redirected to the final link, which is done here.
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers)
    return response.url


def randomvideo(urls):
    #Chooses a random video from Likes.txt - Planned to be optional.
    return random.randint(0, (len(urls) - 1))