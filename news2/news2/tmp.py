from bs4 import BeautifulSoup
import requests
import psycopg2


try:
    con = psycopg2.connect(
        database="news2",
        user="vanpersie05",
        password="dom251212",
        host="127.0.0.1",
        port=""
    )
    cursor = con.cursor()
    #to_insert = (text, url, date)
    #insert_query = """ INSERT INTO fut_news (text, url, pub_date ) VALUES (%s %s %s)"""
    cursor.execute(""" INSERT INTO fut_news (text, url, pub_date ) VALUES (%s %s %s)""")
    con.commit()
except (Exception, psycopg2.Error) as error:
    print("Failed to insert data into database", error)
finally:
    if con:
        cursor.close()
        con.close()
