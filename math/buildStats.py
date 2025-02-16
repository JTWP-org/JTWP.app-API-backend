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

# Define the paths to your input JSON files and the corresponding simple field names
json_files = {
    'math/tempOut/deathCount.json': 'deaths',
    'math/tempOut/deaths.json': 'deaths',
    'math/tempOut/joinCount.json': 'join',
    'math/tempOut/killCount.json': 'kills',
    'math/tempOut/kysCount.json': 'kys',
    'math/tempOut/leftCount.json': 'left',
    'math/tempOut/teamKillCount.json': 'teamkill'
}

# Initialize an empty list to store all players' stats
players_stats_array = []

# Read each JSON file and accumulate stats for each player
for file_name, field_name in json_files.items():
    with open(file_name, 'r') as f:
        data = json.load(f)  # Load JSON data from the file
        for player, count in data.items():
            # Check if the player already exists in the stats array
            player_found = next((p for p in players_stats_array if p['player'] == player), None)
            if player_found:
                # If the player exists, update their stats
                player_found[field_name] = count
            else:
                # If the player doesn't exist, create a new player entry with their stats
                player_stats = {
                    'player': player,
                    field_name: count
                }
                players_stats_array.append(player_stats)

# Ensure that every player has data for all stats (set missing stats to 0)
for player in players_stats_array:
    for field_name in json_files.values():
        if field_name not in player:
            player[field_name] = 0  # Set missing stats to 0

# Specify the output path for the combined JSON
output_file = 'math/tempOut/player_stats.json'

# Save the result as a single JSON array
with open(output_file, 'w') as f:
    json.dump(players_stats_array, f, indent=2)

print(f"Player stats have been saved to '{output_file}'.")

