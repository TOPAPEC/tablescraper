from __future__ import unicode_literals 
import requests
from bs4 import BeautifulSoup
import pandas as pd
import codecs
import sys

baseurl = "http://admlist.ru/index.html"

page = requests.get(baseurl)
page.encoding = 'utf-8'
soup = BeautifulSoup(page.text, "lxml")

refs = soup.find_all("a", href=True)
refs.pop(2)
refs.pop(1)
refs.pop(0)
refs.pop(-1)

mlinks = [] # main links 
for i in refs:
    mlinks.append("http://admlist.ru/" + i.get('href'))
#print(mlinks)

allLinks = []
for clink in mlinks:


    npage = requests.get(clink)
    npage.encoding = 'utf-8'
    nsoup = BeautifulSoup(npage.text, "lxml")

    nrefs = nsoup.find_all("a", href=True)
    nrefs.pop(0)
    nrefs.pop(0)
    nlinks = []
    prefix = clink.replace('index.html', '')
    for i in nrefs:
        nlinks.append(prefix + i.get('href'))
    allLinks += nlinks
#print(allLinks)

file1 = open("links.txt", 'w')

for i in allLinks:
    file1.write("\n")
    file1.write(i)
file1.close()