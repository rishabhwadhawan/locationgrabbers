
file = open('/home/master/authorlocations/newauthors.txt')

i=0
number = 0
writefile = open('/home/master/Downloads/authorfiles/set'+str(number)+"authors.txt",'w')
for lines in file:

    if i == 51:
        number+=1
        writefile = open('/home/master/Downloads/authorfiles/set'+str(number)+"authors.txt",'w')
        i=0
    writefile.write(lines)
    i+=1
