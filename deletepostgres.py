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
# Delete data row from table
cursor.execute("DELETE FROM inventory WHERE name = %s;", ("orange",))
print("Deleted 1 row of data")
# Cleanup
conn.commit()
cursor.close()
conn.close()