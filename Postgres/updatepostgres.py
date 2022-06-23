import psycopg2
from configs import passwords

# Update connection string information
host = "studyserverhh.postgres.database.azure.com"
dbname = "postgres"
user = "Footballstudy"
password = passwords.postgres_password
sslmode = "require"
# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string) 
print("Connection established")
cursor = conn.cursor()
# Update a data row in the table
cursor.execute("UPDATE inventory SET quantity = %s WHERE name = %s;", (200, "banana"))
print("Updated 1 row of data")
# Cleanup
conn.commit()
cursor.close()
conn.close()