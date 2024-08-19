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
import os

def get_columns(schemas, ds_name, sorting_key='column_position'):
    column_details = schemas[ds_name]
    columns = sorted(column_details, key=lambda col: col[sorting_key])
    return [col['column_name'] for col in columns]

def file_converter():
    columns = []
    columns1 = []
    # load schemas for csv files headers
    with open('schemas.json') as headers:
        schemas = json.load(headers)
    
    # list all CSV files in data directory
    files = glob.glob('data/retail_db/*/part*')

    #reading all csv files with columns extracted from schemas.json into pandas dataframe
    for file in files:
        file_details = re.split('/',file)
        ds_name = file_details[2]
        columns = get_columns(schemas,ds_name)
        df = pd.read_csv(file,names=columns)

    #exporting pandas dataframe files into JSON files
        json_file_path_directory = f'data/retail_converted_json/{ds_name}'
        os.makedirs(json_file_path_directory, exist_ok=True)
        json_file_name = f'/{ds_name}.json'
        df.to_json(json_file_path_directory+json_file_name, orient = 'records',lines=True)


file_converter()