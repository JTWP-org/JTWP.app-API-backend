import os
import pandas as pd
import json

def initialize_csv(file_path, columns):
    if not os.path.exists(file_path):
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        df = pd.DataFrame(columns=columns)
        df.to_csv(file_path, index=False)
        print(f"{file_path} initialized.")

def initialize_all_csvs():
    with open("config.json", "r") as f:
        config = json.load(f)
    csv_paths = config["CSV_FILE_PATHS"]

    initialize_csv(csv_paths["DEATH_CSV_FILE"], [
        "timestamp", "killed", "clan", "killer", "headshot", "item",
        "cash", "armor", "health", "score", "killedAtLoc", "levelname"
    ])
    initialize_csv(csv_paths["KILLER_CSV_FILE"], [
        "timestamp", "killer", "clan", "victim", "headshot", "item",
        "cash", "armor", "health", "score", "killedAtLoc", "levelname"
    ])
    initialize_csv(csv_paths["TEAMKILL_CSV_FILE"], [
        "timestamp", "killer", "clan", "killed", "headshot", "item",
        "cash", "armor", "health", "score", "killedAtLoc", "levelname"
    ])
    initialize_csv(csv_paths["KYS_CSV_FILE"], [
        "timestamp", "killer", "clan", "item",
        "cash", "armor", "health", "score", "killedAtLoc", "levelname"
    ])
    initialize_csv(csv_paths["JOIN_CSV_FILE"], [
        "timestamp", "name", "clan", "spawnedAtLoc", "levelname"
    ])
    initialize_csv(csv_paths["LEFT_CSV_FILE"], [
        "timestamp", "name", "clan", "lastAtLoc", "levelname"
    ])

if __name__ == "__main__":
    initialize_all_csvs()
