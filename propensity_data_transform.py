# Robert Jones
# python 3.10.7 64 bit
# 7.8.22, updated 10.11.22
# Working with outreach data for Liz for LIHEAP to
#   ... concatenate and transform all "Propensity" data
#   ... to add date column, dedupe, split names, drop unneeded columns, rearrange and sort columns, save to .csv

import pandas as pd
import glob

global df
df = pd.DataFrame()

class Outreach:

    def __init__(self):
        # Create dataframe from pre-selected path for .csv files
        global df
        # Path to files
        self.path = 'C:/Users/Robert.Jones/OneDrive - Central Coast Energy Services, Inc/Documents/LiHEAP/customer_data'
        # Read all .csv files
        self.csv_files = glob.glob(self.path + '/*.csv')

        # Initialize List
        self.csv_list = []
        # Loop thru csv files
        for i in range(0,len(self.csv_files)):
            # Append the file name
            self.csv_list.append(self.csv_files[i])
            # Append the date (to use in file later)
            self.csv_list.append(self.csv_files[i][-12:-4])

        # Initialize df list
        self.dfs = []
        # Loop thru csv list
        for j in range(0,(len(self.csv_list)-1),2):
            # Open as DF
            df_1 = pd.read_csv(self.csv_list[j])
            # add date column with date from title of document
            df_1['date'] = self.csv_list[j+1]
            # convert to datetime
            df_1['date'] = pd.to_datetime(df_1['date'],format='%b_%Y')
            # Append to list
            self.dfs.append(df_1)


        # Consolidate into one dataframe
        df = pd.concat(self.dfs)



    def initial_explore(self):
        # Print out data before transforming it
        print(df.head(5))
        print(df.shape[0],"rows")
        

    def explore(self):
        # Brief data explore  
        global df
        print(df.head(5))
        print(df.shape[0],"rows")


    def dedupe(self):
        # Deduplicate with pandas method drop_duplicates
        global df
        # to check original # of rows
        original_count = df.shape[0]
        # drop dups on selected column names
        df = df.drop_duplicates(subset=['ACCT_ID','CUSTOMER_NAME'],ignore_index=True)
        # calculate and print dropped rows 
        dropped = original_count - df.shape[0]
        print(f'Duplicates dropped: {dropped}')


    def split_name(self):
        # Split CUSTOMER_NAME into first and last name
        global df
        df['first_name']= df.CUSTOMER_NAME.str.split(',',expand=True)[0]
        df['last_name']= df.CUSTOMER_NAME.str.split(',',expand=True)[1]

    
    def drop_column(self):
        # Drop unnamed columns
        global df
        print(df.head())
        # Drop unnamed columns with a regular expression
        df.drop(df.filter(regex="Unname"),axis=1, inplace=True)


    def arrange_columns(self):
        global df
        # Rearrange name columns to make sense...
        # ... to list 
        column_list = list(df)
        # ... arrange columns
        column_list = column_list[:3] + column_list[-2:] + column_list[5:]
        # ... back into dataframe
        df = df[column_list]
        # drop last two duplicate items that we moved 
        df = df.iloc[:, :-2]

    def sort_values(self):
        # Sort items by date
        global df
        df = df.sort_values(by='date')

    def write(self):
        # Write file to .csv
        global df
        df.to_csv('C:/Users/Robert.Jones/OneDrive - Central Coast Energy Services, Inc/Documents/LiHEAP/transformed_data/propensity_transformed_10.14.22.csv',index=True, index_label="index")
        df.to_csv('C:/Users/Robert.Jones/OneDrive - Central Coast Energy Services, Inc/Documents/LiHEAP/transformed_data/propensity_transformed.csv',index=True, index_label="index")
        



# Create instance of class Outreach
instance = Outreach()
# Check out dataframe before transforming
instance.initial_explore()
# Deduplicate based on [ACCT_ID] and [CUSTOMER_NAME] 
instance.dedupe()
# Split Customer_Name on "," so we have first_name and last_name 
instance.split_name()
# Drop columns by name
instance.drop_column()
# Rearrange columns
instance.arrange_columns()
# Sort data by date
instance.sort_values()
# Explore dataframe before writing
instance.explore()
# Write data to .csv
instance.write()
