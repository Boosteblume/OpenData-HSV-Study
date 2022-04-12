import psycopg2
import pandas as pd
# insert data from csv file into dataframe.
f = "football-data/clean.csv"
df = pd.read_csv(f)

ham_all = df.loc[(df['HomeTeam'] == "Hamburg") | (df['AwayTeam'] == "Hamburg")]
ham_all.fillna(0, inplace = True)

new_df = ham_all[ham_all.columns[0:22]]

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
cursor.execute("CREATE TABLE footballdata (id serial PRIMARY KEY, Div VARCHAR(30), HomeTeam VARCHAR(30), AwayTeam VARCHAR(30), FTHG NUMERIC, FTAG NUMERIC, FTR VARCHAR(30), HTHG NUMERIC, HTAG NUMERIC, HTR VARCHAR(30), HS NUMERIC, ASAS NUMERIC, HST NUMERIC, AST NUMERIC, HF NUMERIC, AF NUMERIC, HC NUMERIC, AC NUMERIC, HY NUMERIC, AY NUMERIC, HR NUMERIC, AR NUMERIC);")
print("Finished creating table")

i = 0 
#Insert Dataframe into SQL Server:
for index, row in new_df.iterrows():
     cursor.execute("INSERT INTO footballdata (Div, HomeTeam, AwayTeam, FTHG, FTAG,FTR,HTHG,HTAG,HTR,HS,ASAS,HST,AST,HF,AF,HC,AC,HY,AY,HR,AR) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (row['Div'], row['HomeTeam'], row['AwayTeam'], row['FTHG'], row['FTAG'], row['FTR'], row['HTHG'], row['HTAG'], row['HTR'], row['HS'], row['ASAS'], row['HST'], row['AST'], row['HF'], row['AF'], row['HC'], row['AC'], row['HY'], row['AY'], row['HR'], row['AR']))
     #testing version
     #cursor.execute("INSERT INTO footballdata (Date, HomeTeam, AwayTeam, FTHG, FTAG,FTR,HTHG,HTAG,HTR,HS,ASAS,HST,AST,HF,AF,HC,AC,HY,AY,HR,AR) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (row['Date'], row['HomeTeam'], row['AwayTeam'], row['FTHG'], row['FTAG'], row['FTR'], row['HTHG'], row['HTAG'], row['HTR'], row['HS'], row['ASAS'], row['HST'], row['AST'], row['HF'], row['AF'], row['HC'], row['AC'], row['HY'], row['AY'], row['HR'], row['AR']))
     
     i = i + 1
     print(i)

print("Finished inserting into table")

# Clean up
conn.commit()
cursor.close()
conn.close()
