import pandas as pd

#This File is just necessary if there are any csv files to merge

#file_list = ["football-data/D2.csv", "football-data/D2-2.csv", "football-data/D2-3.csv", "football-data/D2-4.csv", "football-data/D2-5.csv"]

file_list = ["football-data/D2-5.csv","football-data/D2-4.csv","football-data/D2-3.csv","football-data/D2-2.csv","football-data/D2.csv"]


def merging():
    #Reading the csvs and create a dataframe
    df_list = [pd.read_csv(file) for file in file_list]
    end_df = pd.concat(df_list)
    #Cleaning the dataframes from NaN Values
    end_df.fillna(0, inplace = True)

    end_df = end_df[end_df.columns[0:22]]
    end_df = end_df.rename(columns={'AS':'ASAS'})

    end_df.to_csv("football-data/clean.csv", index=False) 

    print("Dataframe columns:", end_df.columns)

merging()

# df = pd.read_csv("football-data/D2.csv", parse_dates=['Date'])
# print(df.info())
# df.fillna(0, inplace=True)
# #df['Date_conv'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")
# #df.sort_values(by="Date")

# df.to_csv("football-data/test.csv", index=False)

# #print(df[['Date', 'Date_conv']])
