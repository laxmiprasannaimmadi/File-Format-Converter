'''
1. Read csv files from data folder
2. convert csv files using pandas dataframe 
3. convert dataframe files to JSON 
4. Do the validation
'''
import pandas as pd
import glob
import json
import re

def file_converter():
    columns = []
    # load schemas for csv files headers
    with open('schemas.json') as headers:
        schemas = json.load(headers)
    
    # list all CSV files in data directory
    files = glob.glob('data/retail_db/*/part*')

    for file in files:
        file_details = re.split('/',file)
        ds_names = file_details[2]
        column_details = schemas[ds_names]
        for i in range(len(column_details)):
                columns.append(column_details[i]['column_name'])
        print(columns)
        df = pd.read_csv(file,names=columns)
        print(df)

file_converter()