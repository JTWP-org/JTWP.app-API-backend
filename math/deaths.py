import pandas as pd
import json

# Read the CSV file (ensure the path is in quotes)
df = pd.read_csv("data/death_events.csv")

# Clean the 'killer' column by stripping whitespace
df["killed"] = df["killed"].astype(str).str.strip()

# Count occurrences in the 'killer' column
kill_counts = df["killed"].value_counts().to_dict()

# Optionally, convert the counts to an array of integers
kill_counts_array = list(kill_counts.values())

# Output the result as JSON (this will print a JSON object mapping killer names to counts)
print(json.dumps(kill_counts, indent=2))