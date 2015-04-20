import psycopg2

dbname = "authorslocation"
user = "postgres"
password = "data"

def getopenconnection():
    return psycopg2.connect("dbname='" + dbname + "' user='" + user + "' host='localhost' password='" + password + "'")

def create_table(openconnection):
    conn = openconnection
    cur = conn.cursor()
    cur.execute("CREATE TABLE author_tods (Id int, Author varchar);")
    conn.commit()

def insert(id, author,openconnection):
    conn = openconnection
    cur = conn.cursor()
    cur.execute("INSERT INTO author_tods VALUES (%s, %s)",(id, author,))
    conn.commit()

if __name__ == '__main__':
    conn = getopenconnection()
    create_table(conn)
    file = open('/tmp/tods_spatial_postgis.csv')
    id = 0
    authors_list = []
    for lines  in file:
        if(id == 0):
            id += 1
            continue

        else:
            id += 1
            values =lines.split(',')
            author = values[0]
            collaborators = values[1]
            coll = collaborators.split(':')

            length = len(coll)

            j=0
            for i in coll:
                if j == 0:
                    j+=1
                    continue
                else:
                    if i in authors_list:
                        continue
                    else:
                        authors_list.append(i)
    a_id = 0
    for author in authors_list:

        insert(a_id,author, conn)
        a_id+=1

conn.close()