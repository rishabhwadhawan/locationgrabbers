import re
file_a = open('/home/master/authorlocations/icdeuniqueauthors.txt')
file_b = open('/home/master/authorlocations/vldbuniqueauthors.txt')
file_c = open('/home/master/authorlocations/tkdeuniqueauthors.txt')
file_d = open('/home/master/authorlocations/todsuniqueauthors.txt')
file_e = open('/home/master/authorlocations/sigmoduniqueauthors.txt')

writefile = open('/home/master/authorlocations/alluniqueauthors.txt','w')

maindict = {}

for lines_a in file_a:
    lines_a = re.sub('\\n','',lines_a)
    values_a = lines_a.split('$')
    first_author_a = values_a[0]
    latitude_a = values_a[1]
    longitude_a = values_a[2]

    list_a = [latitude_a,longitude_a]
    if first_author_a in maindict.keys():
        continue
    else:
        maindict[first_author_a] = list_a

for lines_b in file_b:
    lines_b = re.sub('\\n','',lines_b)
    values_b = lines_b.split('$')
    first_author_b = values_b[0]
    latitude_b = values_b[1]
    longitude_b = values_b[2]

    list_b = [latitude_b,longitude_b]
    if first_author_b in maindict.keys():
        continue
    else:
        maindict[first_author_b] = list_b

for lines_c in file_c:
    lines_c = re.sub('\\n','',lines_c)
    values_c = lines_c.split('$')
    first_author_c = values_c[0]
    latitude_c = values_c[1]
    longitude_c = values_c[2]

    list_c = [latitude_c,longitude_c]
    if first_author_c in maindict.keys():
        continue
    else:
        maindict[first_author_c] = list_c

for lines_d in file_d:
    lines_d = re.sub('\\n','',lines_d)
    values_d = lines_d.split('$')
    first_author_d = values_d[0]
    latitude_d = values_d[1]
    longitude_d = values_d[2]

    list_d = [latitude_d,longitude_d]
    if first_author_d in maindict.keys():
        continue
    else:
        maindict[first_author_d] = list_d

for lines_e in file_e:
    lines_e = re.sub('\\n','',lines_e)
    values_e = lines_e.split('$')
    first_author_e = values_e[0]
    latitude_e = values_e[1]
    longitude_e = values_e[2]

    list_e = [latitude_e,longitude_e]
    if first_author_e in maindict.keys():
        continue
    else:
        maindict[first_author_e] = list_e

for keys in maindict:

    coordinates = maindict[keys]
    lat = coordinates[0]
    lng = coordinates[1]

    writefile.write(keys)
    writefile.write('$')
    writefile.write(lat)
    writefile.write('$')
    writefile.write(lng)
    writefile.write('\n')

