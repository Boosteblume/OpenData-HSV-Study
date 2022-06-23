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
# Drop previous table of same name if one exists
cursor.execute("DROP TABLE IF EXISTS inventory;")
print("Finished dropping table (if existed)")
# Create a table
cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
print("Finished creating table")
# Insert some data into the table
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
print("Inserted 3 rows of data")
# Clean up
conn.commit()
cursor.close()
conn.close()


connection = psycopg2.connect('host={0} user={1} dbname={2} password={3} sslmode={4}').format(username=username,
                                                                                              password=password,
                                                                                              host=host,
                                                                                              db_name=db_name,
                                                                                              sslmode=sslmode)