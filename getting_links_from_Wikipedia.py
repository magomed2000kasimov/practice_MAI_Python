import requests
from bs4 import BeautifulSoup

html = requests.get('https://ru.wikipedia.org/').text


soup = BeautifulSoup(html, 'lxml')

ul = soup.find('ul','main-wikimedia-list')
print(ul.text)
for elem in ul.find_all('a',{ 'class' : 'extiw'}):
    print(elem['href'])

