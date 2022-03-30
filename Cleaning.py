from ast import Or
import pandas as pd

#This File puts all the values in the dataframe and prints all games where Hamburg played

f = "football-data/clean.csv"

def read():
    df = pd.read_csv(f)

    ham_all = df.loc[(df['HomeTeam'] == "Hamburg") | (df['AwayTeam'] == "Hamburg")]

    print(ham_all)

read()