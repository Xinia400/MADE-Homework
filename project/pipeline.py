import pandas as pd
import requests
from io import BytesIO
import sqlite3
import os
import zipfile
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)
    

def fetch_csv(url, sep=';', encoding='utf-8'):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    df = pd.read_csv(BytesIO(response.content), sep=sep, encoding=encoding)
    return df


def save_sqlite(df, table_name, db_path):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()

def download_zip(url, headers=None):
    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()
    with zipfile.ZipFile(BytesIO(response.content)) as zfile:
        for file_name in zfile.namelist():
            if file_name.endswith('.csv') and 'Europe' in file_name:
                with zfile.open(file_name) as extracted_file:
                    df =  pd.read_csv(extracted_file, encoding='latin1')
    return df


url_1 = 'https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/openaq/exports/csv?lang=en&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B'
url_2 = 'https://bulks-faostat.fao.org/production/Production_Crops_Livestock_E_Europe.zip'

#db_path = os.path.join('../data', 'data_base.db')
sqlite_db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'data_base.db'))
print(f"SQLite DB Path: {sqlite_db_path}")

df1 = fetch_csv(url_1)
df2 = download_zip(url_2)

df2 = df2[['Area', 'Item', 'Element', 'Y2018', 'Y2019', 'Y2020', 'Y2021', 'Y2022']]
df2 = df2.fillna(0)

df2 = df2[df2['Area'] == 'Germany']

df1 = df1[['City', 'Pollutant', 'Value', 'Last Updated','Country Label']]

df1 = df1[df1['Country Label'] == 'Germany']

df1['Last Updated'] = pd.to_datetime(df1['Last Updated'], errors='coerce', utc=True)
df1 = df1[(df1['Last Updated'] >= pd.Timestamp('2018-01-01', tz='UTC')) & (df1['Last Updated'] <= pd.Timestamp('2022-12-31', tz='UTC'))]


df1['Last Updated'] = df1['Last Updated'].dt.year
df1= df1.fillna('Other')

save_sqlite(df1, 'air_quality', sqlite_db_path)
save_sqlite(df2, 'crop_production',sqlite_db_path)
print("Database Stored Successfully")
