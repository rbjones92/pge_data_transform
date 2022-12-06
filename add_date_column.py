# Robert Jones
# 7.12.22
# Add date column for each file. 

import datetime 
import pandas as pd
import os

### Quick script to add date_column to .csv files with a date in the name of the file ### 


# assign directory
os.chdir('C:\\Users\\Robert.Jones\\Documents\\LiHEAP\\customer_data')
directory = 'C:\\Users\\Robert.Jones\\Documents\\LiHEAP\\customer_data'
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if f.endswith('.csv'):
        # Open data in pandas dataframe
        df = pd.read_csv(f)
        # Look at date in filename
        date = filename[-12:-4]
        # Series of conditions to add new "date" column
        if date == "Apr_2022":
            date = datetime.datetime(2022,4,1)
        if date == "May_2022":
            date = datetime.datetime(2022,5,1)
        if date == "Jun_2022":
            date = datetime.datetime(2022,6,1)
        if date == "Mar_2022":
            date = datetime.datetime(2022,3,1)
        if date == "Feb_2022":
            date = datetime.datetime(2022,2,1)
        # add date column to DF
        df['date'] = date
        # write data 
        # df.to_csv(filename)