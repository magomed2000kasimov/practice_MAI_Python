from bs4 import BeautifulSoup
import requests
import re
html = requests.get('https://www.soccer.ru/news').text


soup = BeautifulSoup(html, 'lxml')

ul = soup.find('div', 'view-content')

#for elem in ul.find_all('li'):
#   print(elem['href'])
for elem in ul.find_all('div', { 'class' : 'news'}):
    #tmp = re.search(r'\w+="(\d+-\d+-\d+)"',str(elem.select("meta:nth-of-type(3)")[0]))
    print(elem.select("meta:nth-of-type(3)")[0]['content'],end=' ')
    #print(elem.find_all(name='meta',itemprop="datePublished"))
    #print(tmp.group(1),end=' ')
    print(elem.find('div',{ 'class' : 'created'}).text,end=' ')
    print(elem.a.text)


