from bs4 import BeautifulSoup
import requests
import psycopg2


url = "https://www.weltfussball.de/teams/hamburger-sv/9/"

resp = requests.get(url)

soup =  BeautifulSoup(resp.content)


x = soup.select_one('#site > div.white > div.content > div > div:nth-child(2) > div')

t_list = []

for i in x:
    t_list.append(i.get_text())

t_list = [t.split("\n") for t in t_list]

t_list.pop(0)
t_list.pop(1)

t_list = [tr for t in t_list for tr in t]

res = list(filter(None, t_list))
res = res[4:]

chunks = [res[i:i+2] for i in range(0, len(res), 3)]

chunks = chunks[:21]


#connection settings
host = "studyserverhh.postgres.database.azure.com"
dbname = "postgres"
user = "Footballstudy"
password = "Abstieg2022"
sslmode = "require"
# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string) 
print("Connection established")
cursor = conn.cursor()


#this function is to upload the football-data
def trainer():
    # Drop previous table of same name if one exists
    cursor.execute("DROP TABLE IF EXISTS trainer;")
    print("Finished dropping table (if existed)")


     # Create a table
    cursor.execute("CREATE TABLE trainer (id serial PRIMARY KEY, zeitraum varchar(100), name varchar(50));")
    print("Finished creating table")

    #  i = 0 
    #  #Insert Dataframe into SQL Server:
    #  for i, e in chunks:
    #       cursor.execute("INSERT INTO trainer (zeitraum, name) values (%s, %s);", (i, e))
          
    #       i = i + 1
    #       print(i)

    cursor.executemany("INSERT INTO trainer (zeitraum, name) values (%s, %s);", chunks)
    print("Finished inserting into table")

trainer()

# Clean up
conn.commit()
cursor.close()
conn.close()
