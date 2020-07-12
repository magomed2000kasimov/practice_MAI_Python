from bs4 import BeautifulSoup
import requests
import psycopg2



def insert_into_database(text, url, date):
    try:
        con = psycopg2.connect(
            database="news2",
            user="vanpersie05",
            password="dom251212",
            host="127.0.0.1",
            port=""
        )
        cursor = con.cursor()
        to_insert = (text, url, date)
        insert_query = """ INSERT INTO fut_news (text, url, pub_date ) VALUES (%s, %s, %s)"""
        cursor.execute(insert_query, to_insert)
        con.commit()
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert data into database", error)
    finally:
        if con:
            cursor.close()
            con.close()

html = requests.get('https://www.soccer.ru/news').text

soup = BeautifulSoup(html, 'lxml')

ul = soup.find('div', 'view-content')

#for elem in ul.find_all('li'):
#   print(elem['href'])
for elem in ul.find_all('div', { 'class' : 'news'}):
    #string = elem.select("meta:nth-of-type(3)")[0]['content'] + ' ' + elem.find('div',{ 'class' : 'created'}).text + ' ' + elem.a.text
    date = elem.select("meta:nth-of-type(3)")[0]['content'] + ' ' + elem.find('div',{ 'class' : 'created'}).text
    text = elem.a.text
    url = 'https://www.soccer.ru' + elem.a['href']
    insert_into_database(text, url, date)

