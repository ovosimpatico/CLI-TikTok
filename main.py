from yt_dlp import YoutubeDL
import requests
import os
import random
import subprocess

def listas():
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


def url_redirection(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers)
    return response.url

def removevideo():
    if os.path.exists(os.getcwd()+"/video/video"):
        os.remove(os.getcwd()+"/video/video")
    else:
        pass

def detect_dead_link(url):
    dead_url_start_with = 'https://www.tiktok.com/@/video' 
    #No user on the @ means video was removed, taken down or isn't in a video format
    if dead_url_start_with in url:
        return False # Means do not proceed with the download
    else:
        return True # Means it's all clear to download.

ydl_opts = {
    'ignoreerrors': True,
    'outtmpl': os.getcwd()+'/video/video'
}

urls = listas()[0]
datas = listas()[1]

def main():
    while True:
        removevideo()
        randomvideo = random.randint(0, (len(urls) - 1))
        #os.system("cls || clear")
        url = url_redirection(urls[randomvideo])
        if detect_dead_link(url) == True:
            YoutubeDL(ydl_opts).download(url)
            print(f'\nVideo Liked - {datas[randomvideo]}\n')
            arch = subprocess.check_output(f'mpv --fs "{os.getcwd()}/video/video"', shell=True)
            #os.system(f'mpv --fs "{os.getcwd()}/video/video"')

main()