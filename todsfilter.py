import json
import requests
from lxml import html
import re
import psycopg2

file = open("/home/master/Downloads/tods.json").read()
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
    cur.execute("CREATE TABLE tods (Author varchar , Collaborators varchar, Location varchar, Link varchar, Date varchar, Title varchar,Journal varchar, Volume varchar, Year varchar);")
    conn.commit()
    conn.close()

def insert(author, collaborators, location, link, date, title,journal, volume, year, openconnection):
    conn = openconnection
    cur = conn.cursor()
    cur.execute("INSERT INTO tods VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",(author, collaborators, location, link, date, title,journal, volume, year,))
    conn.commit()

if __name__ == '__main__':
    conn = getopenconnection()

#create_table(conn)

for article in articles:
    authors = ""
    collaborators = article["author"]
    url = str(article["ee"])
    date = article["_mdate"]
    title = str(article["title"])
    journal = str(article["journal"])
    volume = str(article["volume"])
    year = str(article["year"])

    if type(collaborators) is list:
        first_author = collaborators[0]

        for collaborator in collaborators:
            authors += ","+str(collaborator)
    else:
        first_author = collaborators
        authors = 'No collaborator'

    page = requests.get(url)
    tree = html.fromstring(page.text)

    if journal == "ACM Trans. Database Syst.":
        print ("I am running wait....")
        text = tree.xpath("//a[@title = 'Institutional Profile Page']/small/text()")

        global location
        if len(text) == 0:
            continue
        else:
            location = text[0]
        print (location)
    print (first_author)
    print (authors)
    print(url)
    print (date)
    print (title)
    print (journal)
    print (volume)
    print (year)

    insert(first_author, authors, location, url, date, title,journal, volume, year, conn)

conn.close()
