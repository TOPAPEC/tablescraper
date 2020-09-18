from __future__ import unicode_literals
import requests
import lxml.html as lh
import pandas as pd
from bs4 import BeautifulSoup
import codecs




file1 = open('links.txt', 'r')
urllist = file1.readlines()
for i in range(0, len(urllist)):
    urllist[i] = urllist[i][:len(urllist[i]) - 1]
    
file1.close()
# for i in urllist:
#     i.replace('\n', '')


urllist.pop(0) 
print(urllist)
tablelist = pd.DataFrame()

i = 0
for url in urllist:
    page = requests.get(url)
    page.encoding = 'utf-8'
    soup = BeautifulSoup(page.text, "lxml")

    # print(soup.title)

    table = soup.find("table", attrs={"class":"tableFixHead"})
    table_rows = table.find_all('tr')
    table.encoding = 'utf-8'
    #print(table)
    l = []
    for tr in table_rows:
        td = tr.find_all('td')
        row = [tr.text for tr in td]
        l.append(row)
    df = pd.read_html(str(table))
    nd = pd.DataFrame(df[0])
    tablelist = pd.concat([tablelist, df[0]], ignore_index = True)
    if (i % 50 == 0): 
        tablelist.to_excel("output%d.xlsx" %(i))
        tablelist = pd.DataFrame()
    print (i, '\n')
    # nd.to_excel("output%d.xlsx"%(i))
    i += 1 


# pd.concat(tablelist)

# nd = pd.DataFrame(tablelist)  

# nd.to_excel("output.xlsx")

# doc = lh.fromstring(page.content)

# tr_elements = doc.xpath('//tr')

# # print([len(T) for T in tr_elements[:12]])

# col = []
# i = 0

# for t in tr_elements[0]:
#     i+=1
#     name=t.text_content()
#     print ('%d:"%s"'%(i,name))
#     col.append((name,[]))

# for j in range(1, len(tr_elements)): 
#     T=tr_elements[j]
#     if len(T) != 13:
#         break
#     i = 0
#     for t in T.iterchildren():
#         data=t.text_content()
#         if i>0:
#             try:
#                 data=int(data)
#             except:
#                 pass
#         col[i][1].append(data)
#         i+=1

# # print([len(C) for (title,C) in col])

# Dict = {title:column for (title, column) in col}
# df=pd.DataFrame(Dict)

# df.to_excel("output.xlsx")