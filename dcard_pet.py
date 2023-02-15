import requests
import json
from bs4 import BeautifulSoup 

path = open("https://www.dcard.tw/f/pet",'w',encoding='UTF-8')

p = requests.Session()
url = requests.get("https://www.dcard.tw/f/pet")
soup = BeautifulSoup(url.text,"html.parser")

sel = soup.select("div.PostList_wrapper_2BLUM a.PostEntry_root_V6g0r")
a=[]
for s in sel:
    a.append(s["herf"])
url = "https://www.dcard.tw" + a[2]


