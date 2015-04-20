import re
mainfile = open('/home/master/authorlocations/alluniqueauthors.txt')
authorsfile = open('/home/master/authorlocations/Authors.txt')

newauthorfile = open('/home/master/authorlocations/newauthors.txt','w')

authorlist =  set()
for lines_main in mainfile:
    values = lines_main.split('$')
    author = values[0]
    latitude = values[1]
    longitude = values[2]
    authorlist.add(author)

newauthorlist = []
for lines in authorsfile:
    lines = re.sub('\n','',lines)
    if lines in authorlist:
        continue
    else:
        newauthorfile.write(lines)
        newauthorfile.write('\n')
