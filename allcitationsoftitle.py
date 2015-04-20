import json

file = open('/home/master/Downloads/tkde.json').read()

writefile = open("/home/master/tkde_key_title.txt",'w')

data = json.loads(file)
dblp = data["dblp"]

articles = dblp["article"]
i = 1 ;
print (len(articles))
for article in articles:
        if '_key' in article.keys():
            print (i)

        i+=1
        '''
        key = str(article['_key'])
        title = str(article["title"])
        writefile.write(key)
        writefile.write("$")
        writefile.write(title)
        writefile.write("\n")
        '''