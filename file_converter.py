'''
1. Read csv files from data folder
2. convert csv files using pandas dataframe 
3. convert dataframe files to JSON 
4. Do the validation
'''
import pandas as pd
import glob

def file_converter():
    
    # list all CSV files in data directory
    files = glob.glob('data/retail_db/*/part-*')
    for file_name in files:
        df = pd.read_csv(file_name,header=None)
        print(df)

file_converter()