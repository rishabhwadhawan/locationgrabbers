import json
import requests
from lxml import html
import re
import psycopg2

file = open("/home/master/Downloads/tkde.json").read()
data = json.loads(file)
dblp = data["dblp"]
articles = dblp["article"]
location = ""

dbname = "authorslocation"
user = "postgres"
password = "data"

def getopenconnection():
    return psycopg2.connect("dbname='" + dbname + "' user='" + user + "' host='localhost' password='" + password + "'")

def create_table(openconnection):
    conn = openconnection
    cur = conn.cursor()
    cur.execute("CREATE TABLE tkde (Author varchar , Collaborators varchar, Location varchar, Link varchar, Date varchar, Title varchar,Journal varchar, Volume varchar, Year varchar);")
    conn.commit()
    conn.close()

def insert(author, collaborators, location, link, date, title,journal, volume, year, openconnection):
    conn = openconnection
    cur = conn.cursor()
    cur.execute("INSERT INTO tkde VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",(author, collaborators, location, link, date, title,journal, volume, year,))
    conn.commit()

if __name__ == '__main__':
    conn = getopenconnection()

#create_table(conn)
print (len(articles))

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
'''
    page = requests.get(url)
    tree = html.fromstring(page.text)

    text = tree.xpath("//div[@aria-label='Authors Information']/text()")
    text = re.sub('[\\\]','-', str(text))
    text = re.sub('-t','', text)
    text = re.sub('-n','', text)
    text = re.sub('-r','', text)
    text = re.sub('-xa0','', text)
    text = re.sub('[\W]',' ', text)
    text = re.sub(' u ','', text)
    text = text.strip()

    print (first_author)

    if journal == "IEEE Trans. Knowl. Data Eng.":

        print ("I am running wait....")

        global location
        if len(text) == 0:
            continue
        else:
            location = text
        print (location)

    insert(first_author, authors, location, url, date, title,journal, volume, year, conn)
'''
conn.close()
