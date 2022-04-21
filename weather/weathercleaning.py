#datasource https://www.dwd.de/DE/leistungen/klimadatendeutschland/klarchivtagmonat.html => Station Hamburg Fuhlsbüttel

import pandas as pd

file = "klarchiv_01975_daily_his/produkt_klima_tag_19360101_20201231_01975.txt"

df = pd.read_csv(file, sep = ";")

print(df.head())


#Date Umwandlung
df['MESS_DATUM'] = pd.to_datetime(df['MESS_DATUM'], format='%Y%m%d')


#renaming colunmns
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


df = df[df['MESS_DATUM'] >= '1999-01-01']

print(df.columns.values)
