#!/bin/bash

# Directory containing input files
input_dir="./inputs"
# Output file
output_file="results.txt"
# Path to your Python script
script_path="main.py"
# Temporary output file for processing individual input files
temp_output="graph_processing_output.txt"
# Method to use ('fast' or any other for the default method)
method="fast"

# Ensure the output file is empty
> "$output_file"

# Iterate through all input files with a specific extension
for input_file in "$input_dir"/*.txt; do
    # Extract just the filename from the path
    filename=$(basename "$input_file")
    # Process the file with your Python script
    python3 "$script_path" "$input_file" "$temp_output" "$method"
    # Read the number of nodes removed from the temporary output file
    read -r nodes_removed < "$temp_output"
    # Write the input file name and the number of nodes removed to the output file
    echo "$filename, $nodes_removed" >> "$output_file"
done

# Clean up the temporary file
rm "$temp_output"
