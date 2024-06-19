#!/bin/bash

# Run the data pipeline
echo "Running the data pipeline..."
./pipeline.sh

# Check if the output file exists
OUTPUT_FILE="../data/data_base.db"

if [ -f "$OUTPUT_FILE" ]; then
    echo "Database file exists: $OUTPUT_FILE"
else
    echo "Error: Database file does not exist!"
    exit 1
fi

# Run the Python tests
echo "Running the Python tests..."
pytest test.py

echo "All tests completed!"
