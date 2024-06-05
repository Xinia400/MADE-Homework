import requests
import zipfile
import io
import pandas as pd
import sqlite3

# URLs for the datasets
urls = {
    "air_quality": "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/openaq/exports/csv?lang=en&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B",
    "crop_production_fao": "https://bulks-faostat.fao.org/production/Production_Crops_Livestock_E_Europe.zip"
}

# Function to download and read a CSV file directly from URL
def read_csv_from_url(url, sep=';', encoding='utf-8'):
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors
    return pd.read_csv(io.StringIO(response.text), sep=sep, encoding=encoding)

# Function to download and extract a specific file from a ZIP archive
def download_and_extract_csv_from_zip(url):
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors
    with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
        # Identify the CSV file with the expected data
        for file_name in zip_ref.namelist():
            if file_name.endswith('.csv') and 'Europe' in file_name:
                with zip_ref.open(file_name) as extracted_file:
                    return pd.read_csv(extracted_file, encoding='latin1')
    raise ValueError("No suitable CSV file found in the ZIP archive")

# Read air quality data directly from URL
air_quality_data = read_csv_from_url(urls["air_quality"])

# Download and read specific file from crop production data (FAO) ZIP
crop_production_fao_data = download_and_extract_csv_from_zip(urls["crop_production_fao"])

# Filter air quality data for relevant columns and Germany
air_quality_data = air_quality_data[
    ['Country Code', 'City', 'Location', 'Pollutant', 'Value', 'Last Updated']
]
air_quality_data = air_quality_data[air_quality_data['Country Code'] == 'DE']

# Filter crop production data for relevant columns and Germany
crop_production_fao_data = crop_production_fao_data[
    ['Area', 'Item', 'Element', 'Unit', 'Y2018', 'Y2019', 'Y2020', 'Y2021', 'Y2022']
]
crop_production_fao_data = crop_production_fao_data[crop_production_fao_data['Area'] == 'Germany']

# Clean the data (example: handle missing values)
air_quality_data = air_quality_data.dropna()
crop_production_fao_data = crop_production_fao_data.dropna()

# Store the cleaned data in SQLite database
database_path = 'data_analysis.db'
conn = sqlite3.connect(database_path)
air_quality_data.to_sql('air_quality', conn, if_exists='replace', index=False)
crop_production_fao_data.to_sql('crop_production', conn, if_exists='replace', index=False)
conn.close()

# Print success message
print(f"Data pipeline executed successfully.")
