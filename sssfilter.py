import psycopg2

dbname = "authorslocation"
user = "postgres"
password = "data"

def getopenconnection():
    return psycopg2.connect("dbname='" + dbname + "' user='" + user + "' host='localhost' password='" + password + "'")

def create_table(openconnection):
    conn = openconnection
    cur = conn.cursor()
    cur.execute("CREATE TABLE sss (Author varchar , Collaborators varchar, Location varchar, Lat float, Long float, Link varchar, Date varchar, Title varchar,Journal varchar, Volume varchar, Year varchar);")
    conn.commit()
    conn.close()

def insert(author, collaborators, location, latitude, longitude, link, date, title,journal, volume, year, openconnection):
    conn = openconnection
    cur = conn.cursor()
    cur.execute("INSERT INTO sss VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",(author, collaborators, location, latitude, longitude, link, date, title,journal, volume, year,))
    conn.commit()

if __name__ == '__main__':
    conn = getopenconnection()

    cur = conn.cursor()
