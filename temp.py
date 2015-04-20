import re

'''
file = open('/tmp/icde_spatial.csv').read()
file = re.sub(',',':',file)
file = re.sub(';',',',file)

writefile = open('/tmp/icde.csv','w')
writefile.write(file)
'''
filenew = open('/tmp/icde.csv').read()
print filenew