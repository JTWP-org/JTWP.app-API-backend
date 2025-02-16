import pandas as pd
import json

# Read the CSV file
df = pd.read_csv(data/killer_events.csv)

# Clean the killer column (strip whitespace)
df[killer] = df[killer].astype(str).str.strip()

# Count occurrences in the killer column
kill_counts = df[killer].value_counts().to_dict()

# Convert the dictionary values (counts) to a list (array of integers)
kill_counts_array = list(kill_counts.values())

# Output the result as JSON
print(json.dumps(kill_counts, indent=2))



#OUTPUT
#{
#  "test3": 5,
#  "sprucemoose1985": 4,
#  "test1": 1
#}