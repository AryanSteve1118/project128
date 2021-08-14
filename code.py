from bs4 import BeautifulSoup
import csv
import requests
import pandas as pd
import time

URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

r = requests.get(URL)
time.sleep(10)
print(r)
soup = BeautifulSoup(r.text,'html.parser')

table = soup.find_all('table')
print(len(table))
temp = []
rows = table[4].find_all('tr')
for tr in rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp.append(row)
n = []
d = []
m = []
r = []
for i in range(1,len(temp)):
    n.append(temp[i][0])
    m.append(temp[i][5])
    d.append(temp[i][7])
    r.append(temp[i][8])     
df = pd.DataFrame(list(zip(n,d,m,r)),columns = ['name','distance','mass','radius'])    
df.to_csv('final.csv')
#  only four hours of submitting remains
# ok. submit now.. i will check let u know why we r not getting ouput.