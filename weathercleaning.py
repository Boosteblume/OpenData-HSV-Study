#datasource https://www.dwd.de/DE/leistungen/klimadatendeutschland/klarchivtagmonat.html => Station Hamburg Fuhlsbüttel

import pandas as pd

file = "klarchiv_01975_daily_his/produkt_klima_tag_19360101_20201231_01975.txt"

df = pd.read_csv(file, sep = ";")

print(df.head())


#Date Umwandlung funktioniert noch nicht
df['MESS_DATUM'] = pd.to_datetime(df['MESS_DATUM'])

#df = df[df['MESS_DATUM'] >= '1999-01-01']

print(df.head())



