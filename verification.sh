#!/bin/bash

# Path to the single original input file
input_file="./our_input/input_group734.txt"

# Directory containing processed output files
processed_output_dir="./graphs_to_verify"

# Check if the processed_output_dir exists and is a directory
if [ -d "$processed_output_dir" ]; then
    # Loop through each file in the processed output directory
    for processed_file in "$processed_output_dir"/*; do
        # Check if the variable processed_file is a file
        if [ -f "$processed_file" ]; then
            filename=$(basename "$processed_file")

            # Call your Python script to check if the processed graph is a DAG
            # Make sure the Python script is adjusted to accept the single input graph file and a processed output file
            result=$(python3 is_dag.py "$input_file" "$processed_file")
            echo "$filename: $result"
        else
            echo "$processed_file is not a regular file."
        fi
    done
else
    echo "The directory $processed_output_dir does not exist."
fi