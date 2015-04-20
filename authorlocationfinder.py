
file = open('/home/master/Downloads/sigmod_spatial_postgis.csv')
writefile = open('/home/master/sigmoduniqueauthors.txt','w')

dict = {}
i= 0
for lines in file:

    if i==0:
        i+=1
        continue
    values = lines.split('$')
    first_author = values[0]
    latitude = values[2]
    longitude = values[3]
    list = [latitude,longitude]
    if first_author in dict.keys():
        continue
    else:
        dict[first_author] = list

for keys in dict:

    coordinates = dict[keys]
    lat = coordinates[0]
    lng = coordinates[1]

    writefile.write(keys)
    writefile.write('$')
    writefile.write(lat)
    writefile.write('$')
    writefile.write(lng)
    writefile.write('\n')
