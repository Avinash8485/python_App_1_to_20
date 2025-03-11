import requests as r  # used to direct the source page and get the source page aa text of html content
import selectorlib as sl # used to extract perticular informtion from the web page
import smtplib,ssl
import os
import sqlite3 as s
import time


URL = "https://programmer100.pythonanywhere.com/tours/"

connection = s.connect("data.db")


def scrape(url):
    response = r.get(url)
    source = response.text
    return source

def extract(source):
   extractor= sl.Extractor.from_yaml_file("extract.yaml")
   value = extractor.extract(source)["tours"]
   return value

def store(extracted):
    with open("data.txt",'a') as file:
        file.write(extracted+'\n')


def store_sql(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES (?,?,?)",row)
    connection.commit()

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "avinashvel8485@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "avinashvel8485@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

def read(extracted):
    with open("data.txt",'r') as file:
        return file.read()
    
def read_sql(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    brand,city,date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE brand =?and city=? and date=?",(brand,city,date))
    result = cursor.fetchall()
    print(result)
    return result



if __name__ =="__main__":

    #for text
    """while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        
        content = read(extracted)

        if extracted != "No upcoming tours":
            
            if extracted not in "data.txt":
                store(extracted)
                send_email(message="hey new even was found")
        
        time.sleep()"""

    #for sql
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        
        

        if extracted != "No upcoming tours":
            read_sql_data = read_sql(extracted)
            if not read_sql_data:
                store_sql(extracted)
                send_email(message="hey new even was found")
        
        time.sleep()


