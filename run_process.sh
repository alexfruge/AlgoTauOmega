#!/bin/bash

# Directory containing text files
DIRECTORY="inputs"

# Loop through each text file in the directory
for file in "${DIRECTORY}"/*.txt; do
    echo "Processing $file..."
    # Assuming you want the output file to have the same name but with a prefix "processed_"
    input_file=$(basename "$file" .txt)
    # Run the Python script with the current file as input and direct output to a dynamically named file
    python3 main.py "$file" "processed_${input_file}.txt"
done

echo "All files processed."