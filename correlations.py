import psycopg2
from configs import passwords
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm


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


dataFrame = pd.read_sql("SELECT * FROM new_result", conn);

conn.commit()
conn.close()

#print(dataFrame)
print(dataFrame.columns)

df = dataFrame.loc[:, ['tsun', 'hy', 'ay']]

Htgk = df['tsun'].corr(df['hy'])
Atgk = df['tsun'].corr(df['ay'])
htzuat = df['hy'].corr(df['ay'])

print(df.corr())



# Print all rows
# for row in rows:
#     print("Spieldatum = ", row[0] date)
#     print("Sonnenschein = ", row[30] tsun)
#     print("Heimteam gelbe Karten = ", row[17] hy)
#     print("Auswärtsteam gelbe Karten = ", row[18] ay)
