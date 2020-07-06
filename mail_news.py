from bs4 import BeautifulSoup
import requests
import re

html = requests.get('https://news.mail.ru/').text

soup = BeautifulSoup(html, 'lxml')

window = soup.find('div',{ 'class' : 'cols__wrapper'})

for elem in window.find_all('div',class_= ['cols__column', 'cols__column_small_percent-50']):
    print(elem.find('span','hdr__inner').text)
    for mini_elem in elem.find_all('li', class_='list__item'):
        print(mini_elem.text)