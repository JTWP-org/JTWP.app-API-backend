import os
import pandas as pd
import json

# Read the CSV file
df = pd.read_csv('data/join_events.csv')

# Clean the 'killer' column (strip whitespace)
df['name'] = df['name'].astype(str).str.strip()

# Count occurrences in the 'killer' column
kill_counts = df['name'].value_counts().to_dict()

# Convert the dictionary values (counts) to a list (array of integers)
kill_counts_array = list(kill_counts.values())

# Output the result as JSON to the console
print(json.dumps(kill_counts, indent=2))

# Specify the output file path
output_file = 'math/tempOut/joinCount.json'

# Create the directory if it doesn't exist
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Save the result as JSON to a file
with open(output_file, 'w') as file:
    json.dump(kill_counts, file, indent=2)

print(f"JSON data has been saved to {output_file}")

