import json
import os
import subprocess

# List of the other Python scripts to run first
scripts_to_run = [
    'math/deaths.py',
    'math/join.py',
    'math/kills.py',
    'math/kys.py',
    'math/left.py',
    'math/teamKill.py'
]

# Trigger the other scripts before processing the data
for script in scripts_to_run:
    print(f"Running {script}...")
    subprocess.run(['python3', script], check=True)

# Define the paths to your input JSON files
json_files = [
    'math/tempOut/deathCount.json',
    'math/tempOut/deaths.json',
    'math/tempOut/joinCount.json',
    'math/tempOut/killCount.json',
    'math/tempOut/kysCount.json',
    'math/tempOut/leftCount.json',
    'math/tempOut/teamKillCount.json'
]

# Initialize an empty dictionary to store player stats
player_stats = {}

# Read each JSON file and accumulate stats for each player
for file_name in json_files:
    with open(file_name, 'r') as f:
        data = json.load(f)  # Load JSON data from the file
        for player, count in data.items():
            if player not in player_stats:
                player_stats[player] = {}  # Initialize a dictionary for new players
            # Accumulate stats for the player, assigning 0 if the key doesn't exist
            player_stats[player][file_name] = count

# Ensure that every player has data for all stats (set missing stats to 0)
for player, stats in player_stats.items():
    for file_name in json_files:
        if file_name not in stats:
            stats[file_name] = 0  # Set missing stats to 0

# Now, write a separate JSON file for each player
output_dir = 'math/tempOut/Players/'
os.makedirs(output_dir, exist_ok=True)  # Create the directory to store the output files

for player, stats in player_stats.items():
    player_file = os.path.join(output_dir, f"{player}.json")
    with open(player_file, 'w') as f:
        json.dump(stats, f, indent=2)

print(f"Player stats have been saved to the '{output_dir}' directory.")

