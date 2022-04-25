#datasource https://www.dwd.de/DE/leistungen/klimadatendeutschland/klarchivtagmonat.html => Station Hamburg Fuhlsbüttel
import psycopg2
import pandas as pd
import os

# file = r"weather\Lufttemperatur\regional_averages_tm_01.txt"

# df = pd.read_csv(file, skiprows=1, sep = ";")

# print(df.keys())
# print(df["Niedersachsen/Hamburg/Bremen"])


#Step1 merging into one clean file

file_list = [] 
for i in os.listdir(r"weather\Sonnenscheindauer"):
    if i.endswith(".txt"):
        i = "weather/Sonnenscheindauer/" + i
        file_list.append(i)


df_list = [pd.read_csv(file, skiprows=1, sep = ";") for file in file_list]
end_df = pd.concat(df_list)

#Cleaning the dataframes from NaN Values
end_df.fillna(0, inplace = True)

end_df = end_df[end_df.columns[0:10]]
end_df = end_df[end_df['Jahr'] > 2010]
end_df = end_df.rename(columns={'Niedersachsen/Hamburg/Bremen':'Hamburg'})

#end_df.to_csv("weather/clean.csv", index=False) 

print("Dataframe columns:", end_df.columns)




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
def temperatur():
     # Drop previous table of same name if one exists
     cursor.execute("DROP TABLE IF EXISTS sonnenschein;")
     print("Finished dropping table (if existed)")


     # Create a table
     cursor.execute("CREATE TABLE sonnenschein (id serial PRIMARY KEY, Jahr VARCHAR(10), Monat VARCHAR(5), Hamburg VARCHAR(10));")
     print("Finished creating table")

     i = 0 
     #Insert Dataframe into SQL Server:
     for index, row in end_df.iterrows():
          cursor.execute("INSERT INTO sonnenschein (Jahr, Monat, Hamburg) values (%s, %s, %s);", (row['Jahr'], row['Monat'], row['Hamburg']))
        
          i = i + 1
          print(i)

     print("Finished inserting into table")

temperatur()



# Clean up
conn.commit()
cursor.close()
conn.close()
