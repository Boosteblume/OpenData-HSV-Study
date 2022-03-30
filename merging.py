import pandas as pd

#This File is just necessary if there are any csv files to merge

file_list = ["football-data/D2.csv", "football-data/D2-2.csv", "football-data/D2-3.csv", "football-data/D2-4.csv", "football-data/D2-5.csv"]

def merging():
    #Reading the csvs and create a dataframe
    df_list = [pd.read_csv(file) for file in file_list]
    end_df = pd.concat(df_list)
    #Cleaning the dataframes from NaN Values
    end_df.to_csv("football-data/clean.csv", index=False) 

merging()