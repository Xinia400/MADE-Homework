import sqlite3
import pytest
import os

# Define the path to the SQLite database
db_path = os.path.join(os.path.dirname(__file__), '../data/data_base.db')

@pytest.fixture
def db_cursor():
    db_connection = sqlite3.connect(db_path)
    cursor = db_connection.cursor()
    yield cursor
    db_connection.close()

@pytest.fixture
def db_connection():
    if not os.path.isfile(db_path):
        pytest.fail(f"Error: The specified path '{db_path}' does not exist or is not a regular file path.")
    try:
        connection = sqlite3.connect(db_path)
        yield connection
    finally:
        connection.close()

def test_valid_sqlite_database(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    assert len(tables) > 0, "The database does not contain any tables, hence it is not a valid SQLite database."

def test_tables_exist(db_cursor):
    db_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = db_cursor.fetchall()
    assert ("air_quality",) in tables, "Table 'air_quality' does not exist in the database!"
    assert ("crop_production",) in tables, "Table 'crop_production' does not exist in the database!"

def extract_column_info(columns):
    return [(name, type_) for _, name, type_, _, _, _ in columns]

@pytest.mark.parametrize("table_name, expected_columns", [
    ("air_quality", [
        ("City", "TEXT"),
        ("Pollutant", "TEXT"),
        ("Value", "REAL"),
        ("Last Updated", "INTEGER"),
        ("Country Label", "TEXT"),
    ]),
    ("crop_production", [
        ("Area", "TEXT"),
        ("Item", "TEXT"),
        ("Element", "TEXT"),
        ("Y2018", "REAL"),
        ("Y2019", "REAL"),
        ("Y2020", "REAL"),
        ("Y2021", "REAL"),
        ("Y2022", "REAL"),
    ])
])
def test_table_columns(db_cursor, table_name, expected_columns):
    db_cursor.execute(f"PRAGMA table_info({table_name});")
    columns = db_cursor.fetchall()
    extracted_columns = extract_column_info(columns)
    for column, data_type in expected_columns:
        assert (column, data_type) in extracted_columns, f"Column '{column}' with type '{data_type}' not found in table '{table_name}'"

@pytest.mark.parametrize("table_name", ["air_quality", "crop_production"])
def test_table_data(db_cursor, table_name):
    db_cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
    count = db_cursor.fetchone()[0]
    assert count > 0, f"Table '{table_name}' is empty!"

@pytest.mark.parametrize("table_name, column_name, min_value, max_value", [
    ("air_quality", "Value", 0, 10000),  # Assuming pollutant values are within this range
    ("crop_production", "Y2018", 0, 120000000),  # Adjusted maximum value based on actual data
    ("crop_production", "Y2019", 0, 120000000),  # Adjusted maximum value based on actual data
    ("crop_production", "Y2020", 0, 120000000),  # Adjusted maximum value based on actual data
    ("crop_production", "Y2021", 0, 120000000),  # Adjusted maximum value based on actual data
    ("crop_production", "Y2022", 0, 120000000),  # Adjusted maximum value based on actual data
])
def test_data_validity(db_cursor, table_name, column_name, min_value, max_value):
    query = f"SELECT {column_name} FROM {table_name} WHERE {column_name} NOT BETWEEN ? AND ?;"
    db_cursor.execute(query, (min_value, max_value))
    invalid_values = db_cursor.fetchall()
    assert len(invalid_values) == 0, f"Found invalid values in column {column_name} of table {table_name}"

if __name__ == "__main__":
    pytest.main()
