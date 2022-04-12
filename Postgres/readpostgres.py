import psycopg2
# Update connection string information
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
# Fetch all rows from table
cursor.execute("SELECT * FROM footballdata Where hometeam = 'Hamburg';")
rows = cursor.fetchall()

# Print all rows
for row in rows:
    print("id = ", row[0])
    print("div = ", row[1])
    print("hometeam = ", row[2])
    print("awayteam = ", row[3])
    print("fthg = ", row[4])
    print("ftag = ", row[5])
    print("ftr = ", row[6])
    print("hthg = ", row[7])
    print("htag = ", row[8])
    print("htr = ", row[9])
    print("hs = ", row[10])
    print("as = ", row[11])
    print("hst = ", row[12])
    print("ast = ", row[13])
    print("hf = ", row[14])
    print("af = ", row[15])
    print("hc = ", row[16])
    print("ac = ", row[17])
    print("hy = ", row[18])
    print("ay = ", row[19])
    print("hr = ", row[20])
    print("ar = ", row[21])

# Cleanups
conn.commit()
cursor.close()
conn.close()