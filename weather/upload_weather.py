import psycopg2
import pandas as pd

# insert data from csv file into dataframe.
file = "klarchiv_01975_daily_his/produkt_klima_tag_19360101_20201231_01975.txt"
df = pd.read_csv(file, sep = ";")

df['MESS_DATUM'] = pd.to_datetime(df['MESS_DATUM'], format='%Y%m%d')

df.rename(columns = {'  FX': 'FX'}, inplace = True)
df.rename(columns = {'  FM': 'FM'}, inplace = True)
df.rename(columns = {' RSK': 'RSK'}, inplace = True)
df.rename(columns = {' SDK': 'SDK'}, inplace = True)
df.rename(columns = {'  NM': 'NM'}, inplace = True)
df.rename(columns = {' VPM': 'VPM'}, inplace = True)
df.rename(columns = {'  PM': 'PM'}, inplace = True)
df.rename(columns = {' TMK': 'TMK'}, inplace = True)
df.rename(columns = {' UPM': 'UPM'}, inplace = True)
df.rename(columns = {' TXK': 'TXK'}, inplace = True)
df.rename(columns = {' TNK': 'TNK'}, inplace = True)
df.rename(columns = {' TGK': 'TGK'}, inplace = True)

df = df[df['MESS_DATUM'] >= '2017-01-01']


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


#this function is to upload the football-data
def weather():
     # Drop previous table of same name if one exists
     cursor.execute("DROP TABLE IF EXISTS weather;")
     print("Finished dropping table (if existed)")


     # Create a table
     cursor.execute("CREATE TABLE weather (id serial PRIMARY KEY, STATIONS_ID NUMERIC, MESS_DATUM VARCHAR(50), QN_3 VARCHAR(50), FX VARCHAR(50), FM VARCHAR(50), QN_4 VARCHAR(50), RSK VARCHAR(50), RSKF VARCHAR(50), SDK VARCHAR(50), SHK_TAG VARCHAR(50), NM VARCHAR(50), VPM VARCHAR(50), PM VARCHAR(50), TMK VARCHAR(50), UPM VARCHAR(50), TXK VARCHAR(50), TNK VARCHAR(50), TGK VARCHAR(50));")
     print("Finished creating table")

     i = 0 
     #Insert Dataframe into SQL Server:
     for index, row in df.iterrows():
          cursor.execute("INSERT INTO weather (STATIONS_ID, MESS_DATUM, QN_3, FX, FM, QN_4, RSK, RSKF, SDK, SHK_TAG, NM, VPM, PM, TMK, UPM, TXK, TNK, TGK) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (row['STATIONS_ID'], row['MESS_DATUM'], row['QN_3'], row['FX'], row['FM'], row['QN_4'], row['RSK'], row['RSKF'], row['SDK'], row['SHK_TAG'], row['NM'], row['VPM'], row['PM'], row['TMK'], row['UPM'], row['TXK'], row['TNK'], row['TGK']))
          i = i + 1
          print(i)

     print("Finished inserting into table")

weather()

# Clean up
conn.commit()
cursor.close()
conn.close()
