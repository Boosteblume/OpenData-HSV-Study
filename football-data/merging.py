import pandas as pd
import os

#This File is just necessary if there are any csv files to merge

#file_list = ["football-data/D2-5.csv","football-data/D2-4.csv","football-data/D2-3.csv","football-data/D2-2.csv","football-data/D2.csv"]

# file_list = [] 
# for i in os.listdir(r"football-data"):
#     if i.endswith(".csv"):
#         i = "football-data/" + i
#         file_list.append(i)


# def merging():
#     #Reading the csvs and create a dataframe
#     df_list = [pd.read_csv(file) for file in file_list]
#     end_df = pd.concat(df_list)
#     #Cleaning the dataframes from NaN Values
#     end_df.fillna(0, inplace = True)

#     end_df = end_df[end_df.columns[0:22]]
#     end_df = end_df.rename(columns={'AS':'ASAS'})

#     end_df.to_csv("football-data/clean.csv", index=False) 

#     print("Dataframe columns:", end_df.columns)

# merging()


file_list = []
file_list_d1 = [] 
file_list_d2 = []

for i in os.listdir(r"football-data"):
    if i.endswith(".csv"):
        print(i)


#if it would be necessary to split
        if i.startswith("football-data/D1"):
            file_list_d1.append(i)
        elif i.startswith("D2"):
            file_list_d2.append("football-data/" + i)

#
#   NOT DONE YET DATE STILL FUCKED UP
#
def merging(file_list):
    global end_df
    #Reading the csvs and create a dataframe
    df_list = [pd.read_csv(file) for file in file_list]
    end_df = pd.concat(df_list)
    #Cleaning the dataframes from NaN Values
    end_df.fillna(0, inplace = True)
    if file_list == file_list_d1:
        i = 1
    else:
        i = 2
    #Sorting the df and changing the date format
    end_df = end_df[end_df.columns[0:23]]
    end_df = end_df.rename(columns={'AS':'ASAS'})
    end_df['Date'] = pd.to_datetime(end_df['Date'], infer_datetime_format=True)
    end_df = end_df.sort_values(by="Date", ascending=True)

    end_df.to_csv(f"football-data/clean{i}.csv", index=False) 


#merging(file_list_d1)
merging(file_list_d2)

# df1 = pd.read_csv("football-data/clean1.csv")
# df2 = pd.read_csv("football-data/clean2.csv")
# dfl = [df1, df2]
# df = pd.concat(dfl)
# df.to_csv("football-data/result.csv")