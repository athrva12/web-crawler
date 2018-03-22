
import requests
from bs4 import BeautifulSoup
def info(max_pages):
    page=1
    while (page<=max_pages):
        count=0
        url='https://www.codechef.com/FEB18/status/PERMPAL'
        source= requests.get(url)
        plain=source.text
        soup=BeautifulSoup(plain)
        for link in soup.findAll('a'):
            href=link.get('href')
            print(href)



            count=count+1

        print(count)
        page+=1
info(1)

