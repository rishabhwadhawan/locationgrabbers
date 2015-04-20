import geocoder
import time

file = open('/home/master/Downloads/demoauthors_location.txt')
writefile = open('/home/master/Downloads/mtec2.txt','w')

for lines in file:

        value = lines.split("$")

        name = value[0]
        address = value[1]

        location = geocoder.google(address)

        latitude = location.lat
        longitude = location.lng


        if latitude is None or longitude is None:
            time.sleep(5)
            continue
        else:
            print (name)
            print (address)
            print (latitude)
            print (longitude)
            writefile.write(name)
            writefile.write('$')
            writefile.write(str(address))
            writefile.write('$')
            writefile.write(str(latitude))
            writefile.write('$')
            writefile.write(str(longitude))
            writefile.write('\n')
            time.sleep(5)
