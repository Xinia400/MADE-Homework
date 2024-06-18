#!/bin/bash

# Run the data pipeline
echo "Running the data pipeline..."
python3 pipeline.py

# Check if the output files exist
OUTPUT_DIR="../data"
DB_FILE="$OUTPUT_DIR/data_base.db"

if [ -f "$DB_FILE" ]; then
    echo "Database file exists: $DB_FILE"
else
    echo "Error: Database file does not exist!"
    exit 1
fi

echo "All tests passed successfully!"
