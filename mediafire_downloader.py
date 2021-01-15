#author: GanciDev
import requests 
import urllib.request
from bs4 import BeautifulSoup

def download_rar(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)

url = open("/path_to_the_file/link_mediafire.txt", "r").readlines()
cont=1
for l in url:
    l=str(l).replace("\n","")
    if l!="":
        site=urllib.request.urlopen(l)
        site = urllib.request.urlopen(str(l))
        html = site.read()
        soup = BeautifulSoup(html)
        list_urls = soup.find_all('a')
        component=str(list_urls[7]).split(" ")
        component=str(component[5]).split("=")
        link=str(component[1]).replace('"',"")
        print(str(cont)+":"+link)
        download_rar(link,"NameFile"+str(cont)+".rar")
    cont=cont+1