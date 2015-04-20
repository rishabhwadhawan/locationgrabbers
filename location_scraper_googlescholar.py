import re
import requests
from lxml import html
import time

dbname = "authorslocation"
user = "postgres"
password = "data"


#    create_table(conn)

file = open('/home/master/Downloads/file2.txt')
writefile = open('/home/master/Downloads/demotempauthors8_location.txt','w')
for lines in file:
    lines = re.sub("[\W]"," ",lines)
    lines = re.sub("  "," ",lines)
    lines = lines.strip()
    author = lines

    print ('-')
    name = re.sub(" ","+",lines)
    print (name)

    url = 'http://scholar.google.com/scholar?hl=en&q='+str(name)
    page = requests.get(url)
    tree = html.fromstring(page.text)
    text = tree.xpath("//div[@class='gs_nph']/text()")
    print (text)
    if len(text) == 0:
        continue
    else:
        if "," in text[0]:
            values = text[0].split(', ')
            location = values[1]
        else:
            location = text[0]
    print (author)
    print (location)

    writefile.write(author)
    writefile.write('$')
    writefile.write(location)
    writefile.write('\n')