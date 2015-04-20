import json
import requests
from lxml import html
import re
import psycopg2

file = open("/home/master/Downloads/sigmod.json").read()
data = json.loads(file)
dblp = data["dblp"]
articles = dblp["article"]
location = ""
dbname = "authorslocation"
user = "postgres"
password = "data"

print (len(articles))
def getopenconnection():
    return psycopg2.connect("dbname='" + dbname + "' user='" + user + "' host='localhost' password='" + password + "'")

def create_table(openconnection):
    conn = openconnection
    cur = conn.cursor()
    cur.execute("CREATE TABLE sigmod (Author varchar , Location varchar, Link varchar, Date varchar, Title varchar,Journal varchar);")
    conn.commit()
    conn.close()

def delete_table(openconnection):
    conn = openconnection
    cur = conn.cursor()
    cur.execute("DROP TABLE sigmod;")
    conn.commit()
    conn.close()

def insert(author, location, link, date, title,journal, openconnection):
    conn = openconnection
    cur = conn.cursor()
    cur.execute("INSERT INTO sigmod VALUES (%s, %s, %s, %s, %s, %s)",(author, location, link, date, title,journal,))
    conn.commit()

if __name__ == '__main__':
    conn = getopenconnection()

#create_table(conn)
print (len(articles))
i=0
for article in articles:
    authors = article["author"]
    url = str(article["ee"])
    date = article["_mdate"]
    title = str(article["title"])
    journal = str(article["journal"])

    if type(authors) is list:
        first_author = authors[0]
        i+=1
    else:
        first_author = authors
        i+=1
    print (first_author)
    print(i)

    page = requests.get(url)
    tree = html.fromstring(page.text)

    if journal == "SIGMOD Record":
        print ("I am running wait....")
        text = tree.xpath("//a[@title = 'Institutional Profile Page']/small/text()")

        global location
        if len(text) == 0:
            continue
        else:
            location = text[0]
        print (location)

    i += 1
   #insert(first_author, location, url, date, title,journal,conn)

print(i)
conn.close()
