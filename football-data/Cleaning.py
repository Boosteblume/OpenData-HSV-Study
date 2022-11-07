import pandas as pd

#This File puts all the values in the dataframe and prints all games where Hamburg played

f = "football-data/clean2.csv"

def read():
    df = pd.read_csv(f)

    ham_all = df.loc[(df['HomeTeam'] == "Hamburg") | (df['AwayTeam'] == "Hamburg")]
    ham_all.fillna(0, inplace = True)

    new_df = ham_all[ham_all.columns[0:22]]
    row_1=new_df.iloc[0]

    print(new_df)


read()