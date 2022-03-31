import psycopg2
import pandas as pd
# insert data from csv file into dataframe.
f = "football-data/clean.csv"
df = pd.read_csv(f)
df_ham = df.loc[(df['HomeTeam'] == "Hamburg") | (df['AwayTeam'] == "Hamburg")]

# Some other example server values are
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

# Drop previous table of same name if one exists
cursor.execute("DROP TABLE IF EXISTS footballdata;")
print("Finished dropping table (if existed)")

# Create a table
cursor.execute("CREATE TABLE footballdata (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
print("Finished creating table")

# Insert Dataframe into SQL Server:
for index, row in df.iterrows():
     cursor.execute("INSERT INTO HumanResources.DepartmentTest (DepartmentID,Name,GroupName) values(?,?,?)", row.DepartmentID, row.Name, row.GroupName)

# Clean up
conn.commit()
cursor.close()
conn.close()



# Insert some data into the table
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
print("Inserted 3 rows of data")

"CREATE TABLE footballdata (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")

CREATE TABLE footballdata(
id serial PRIMARY KEY,
Div varchar(2),
Date TYP,
Time TYP,
HomeTeam TYP,
AwayTeam TYP,
FTHG TYP,
FTAG TYP,
FTR TYP,
HTHG TYP,
HTAG TYP,
HTR TYP,
HS TYP,
AS TYP,
HST TYP,
AST TYP,
HF TYP,
AF TYP,
HC TYP,
AC TYP,
HY TYP,
AY TYP,
HR TYP,
AR TYP
)
;
