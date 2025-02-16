from flask import Flask, request, jsonify
import pandas as pd
from datetime import datetime
import os

app = Flask(__name__)

# Expected API key (keep this secret!)
API_KEY = "58d577a8107f2cffb67ec5d278139f76"

# CSV file paths for each event type
DEATH_CSV_FILE = 'death_events.csv'
KILLER_CSV_FILE = 'killer_events.csv'
TEAMKILL_CSV_FILE = 'teamkill_events.csv'
KYS_CSV_FILE = 'kys_events.csv'
JOIN_CSV_FILE = 'join_events.csv'
LEFT_CSV_FILE = 'left_events.csv'

# Utility function to initialize a CSV file if it doesn't exist
def initialize_csv(file_path, columns):
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=columns)
        df.to_csv(file_path, index=False)
        print(f"{file_path} initialized.")

# Initialize CSVs for each event type
initialize_csv(DEATH_CSV_FILE, [
    "timestamp", "killed", "clan", "killer", "headshot", "item",
    "cash", "armor", "health", "score", "killedAtLoc", "levelname"
])
initialize_csv(KILLER_CSV_FILE, [
    "timestamp", "killer", "clan", "victim", "headshot", "item",
    "cash", "armor", "health", "score", "killedAtLoc", "levelname"
])
initialize_csv(TEAMKILL_CSV_FILE, [
    "timestamp", "killer", "clan", "killed", "headshot", "item",
    "cash", "armor", "health", "score", "killedAtLoc", "levelname"
])
initialize_csv(KYS_CSV_FILE, [
    "timestamp", "killer", "clan", "item",
    "cash", "armor", "health", "score", "killedAtLoc", "levelname"
])
initialize_csv(JOIN_CSV_FILE, [
    "timestamp", "name", "clan", "spawnedAtLoc", "levelname"
])
initialize_csv(LEFT_CSV_FILE, [
    "timestamp", "name", "clan", "lastAtLoc", "levelname"
])

# Utility function to read a CSV file
def read_csv_file(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return pd.DataFrame()

# Utility function to append new data to a CSV file
def append_data_to_csv(file_path, new_data):
    try:
        df = read_csv_file(file_path)
        new_df = pd.DataFrame([new_data])
        df = pd.concat([df, new_df], ignore_index=True)
        df.to_csv(file_path, index=False)
        print(f"Data added to {file_path}.")
    except Exception as e:
        print(f"Error appending data to {file_path}: {e}")

# API key check function
def check_api_key():
    api_key = request.headers.get('X-API-Key')
    if api_key != API_KEY:
        return jsonify({"error": "Unauthorized access. Invalid API key."}), 401

#####################
# POST Endpoints
#####################

# Submit Death Event
@app.route('/api/submit_death', methods=['POST'])
def submit_death():
    api_key_check = check_api_key()
    if api_key_check:
        return api_key_check
    payload = request.get_json()
    if not payload or "deathEvent" not in payload:
        return jsonify({"error": "Missing deathEvent in payload"}), 400

    death_event = payload["deathEvent"]
    timestamp = death_event.get("timeStamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    event_detail = death_event.get("eventDetail", [])
    if not event_detail or not isinstance(event_detail, list):
        return jsonify({"error": "Missing or invalid eventDetail"}), 400
    detail = event_detail[0]
    killed = detail.get("name", "")
    clan = detail.get("clan", "")
    killer = detail.get("killer", "")
    headshot = detail.get("headshot", False)
    item = detail.get("item", "")
    stats = death_event.get("stats", [])
    if not stats or not isinstance(stats, list):
        return jsonify({"error": "Missing or invalid stats"}), 400
    stat = stats[0]
    cash = stat.get("cash", 0)
    armor = stat.get("armor", 0)
    health = stat.get("health", 0)
    score = stat.get("score", 0)
    killedAtLoc = stat.get("killedAtLoc", "")
    levelname = stat.get("levelname", "")
    new_data = {
        "timestamp": timestamp,
        "killed": killed,
        "clan": clan,
        "killer": killer,
        "headshot": headshot,
        "item": item,
        "cash": cash,
        "armor": armor,
        "health": health,
        "score": score,
        "killedAtLoc": killedAtLoc,
        "levelname": levelname
    }
    append_data_to_csv(DEATH_CSV_FILE, new_data)
    return jsonify({"message": "Death event processed", "data": payload}), 200

# Submit Killer Event
@app.route('/api/submit_killer', methods=['POST'])
def submit_killer():
    api_key_check = check_api_key()
    if api_key_check:
        return api_key_check
    payload = request.get_json()
    if not payload or "killerEvent" not in payload:
        return jsonify({"error": "Missing killerEvent in payload"}), 400

    killer_event = payload["killerEvent"]
    timestamp = killer_event.get("timeStamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    event_detail = killer_event.get("eventDetail", [])
    if not event_detail or not isinstance(event_detail, list):
        return jsonify({"error": "Missing or invalid eventDetail"}), 400
    detail = event_detail[0]
    killer = detail.get("name", "")
    clan = detail.get("clan", "")
    victim = detail.get("victim", "")
    headshot = detail.get("headshot", False)
    item = detail.get("item", "")
    stats = killer_event.get("stats", [])
    if not stats or not isinstance(stats, list):
        return jsonify({"error": "Missing or invalid stats"}), 400
    stat = stats[0]
    cash = stat.get("cash", 0)
    armor = stat.get("armor", 0)
    health = stat.get("health", 0)
    score = stat.get("score", 0)
    killedAtLoc = stat.get("killedAtLoc", "")
    levelname = stat.get("levelname", "")
    new_data = {
        "timestamp": timestamp,
        "killer": killer,
        "clan": clan,
        "victim": victim,
        "headshot": headshot,
        "item": item,
        "cash": cash,
        "armor": armor,
        "health": health,
        "score": score,
        "killedAtLoc": killedAtLoc,
        "levelname": levelname
    }
    append_data_to_csv(KILLER_CSV_FILE, new_data)
    return jsonify({"message": "Killer event processed", "data": payload}), 200

# Submit Teamkill Event
@app.route('/api/submit_teamkill', methods=['POST'])
def submit_teamkill():
    api_key_check = check_api_key()
    if api_key_check:
        return api_key_check
    payload = request.get_json()
    if not payload or "teamKillEvent" not in payload:
        return jsonify({"error": "Missing teamKillEvent in payload"}), 400

    teamkill_event = payload["teamKillEvent"]
    timestamp = teamkill_event.get("timeStamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    event_detail = teamkill_event.get("eventDetail", [])
    if not event_detail or not isinstance(event_detail, list):
        return jsonify({"error": "Missing or invalid eventDetail"}), 400
    detail = event_detail[0]
    killer = detail.get("name", "")
    clan = detail.get("clan", "")
    killed = detail.get("killed", "")
    headshot = detail.get("headshot", False)
    item = detail.get("item", "")
    stats = teamkill_event.get("stats", [])
    if not stats or not isinstance(stats, list):
        return jsonify({"error": "Missing or invalid stats"}), 400
    stat = stats[0]
    cash = stat.get("cash", 0)
    armor = stat.get("armor", 0)
    health = stat.get("health", 0)
    score = stat.get("score", 0)
    killedAtLoc = stat.get("killedAtLoc", "")
    levelname = stat.get("levelname", "")
    new_data = {
        "timestamp": timestamp,
        "killer": killer,
        "clan": clan,
        "killed": killed,
        "headshot": headshot,
        "item": item,
        "cash": cash,
        "armor": armor,
        "health": health,
        "score": score,
        "killedAtLoc": killedAtLoc,
        "levelname": levelname
    }
    append_data_to_csv(TEAMKILL_CSV_FILE, new_data)
    return jsonify({"message": "Teamkill event processed", "data": payload}), 200

# Submit KYS Event
@app.route('/api/submit_kys', methods=['POST'])
def submit_kys():
    api_key_check = check_api_key()
    if api_key_check:
        return api_key_check
    payload = request.get_json()
    if not payload or "kysEvent" not in payload:
        return jsonify({"error": "Missing kysEvent in payload"}), 400

    kys_event = payload["kysEvent"]
    timestamp = kys_event.get("timeStamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    event_detail = kys_event.get("eventDetail", [])
    if not event_detail or not isinstance(event_detail, list):
        return jsonify({"error": "Missing or invalid eventDetail"}), 400
    detail = event_detail[0]
    killer = detail.get("name", "")
    clan = detail.get("clan", "")
    item = detail.get("item", "")
    stats = kys_event.get("stats", [])
    if not stats or not isinstance(stats, list):
        return jsonify({"error": "Missing or invalid stats"}), 400
    stat = stats[0]
    cash = stat.get("cash", 0)
    armor = stat.get("armor", 0)
    health = stat.get("health", 0)
    score = stat.get("score", 0)
    killedAtLoc = stat.get("killedAtLoc", "")
    levelname = stat.get("levelname", "")
    new_data = {
        "timestamp": timestamp,
        "killer": killer,
        "clan": clan,
        "item": item,
        "cash": cash,
        "armor": armor,
        "health": health,
        "score": score,
        "killedAtLoc": killedAtLoc,
        "levelname": levelname
    }
    append_data_to_csv(KYS_CSV_FILE, new_data)
    return jsonify({"message": "KYS event processed", "data": payload}), 200

# Submit Join Event
@app.route('/api/submit_join', methods=['POST'])
def submit_join():
    api_key_check = check_api_key()
    if api_key_check:
        return api_key_check
    payload = request.get_json()
    if not payload or "joinEvent" not in payload:
        return jsonify({"error": "Missing joinEvent in payload"}), 400

    join_event = payload["joinEvent"]
    timestamp = join_event.get("timeStamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    event_detail = join_event.get("eventDetail", [])
    if not event_detail or not isinstance(event_detail, list):
        return jsonify({"error": "Missing or invalid eventDetail"}), 400
    detail = event_detail[0]
    name = detail.get("name", "")
    clan = detail.get("clan", "")
    stats = join_event.get("stats", [])
    if not stats or not isinstance(stats, list):
        return jsonify({"error": "Missing or invalid stats"}), 400
    stat = stats[0]
    spawnedAtLoc = stat.get("spawnedAtLoc", "")
    levelname = stat.get("levelname", "")
    new_data = {
        "timestamp": timestamp,
        "name": name,
        "clan": clan,
        "spawnedAtLoc": spawnedAtLoc,
        "levelname": levelname
    }
    append_data_to_csv(JOIN_CSV_FILE, new_data)
    return jsonify({"message": "Join event processed", "data": payload}), 200

# Submit Left Event
@app.route('/api/submit_left', methods=['POST'])
def submit_left():
    api_key_check = check_api_key()
    if api_key_check:
        return api_key_check
    payload = request.get_json()
    if not payload or "leftEvent" not in payload:
        return jsonify({"error": "Missing leftEvent in payload"}), 400

    left_event = payload["leftEvent"]
    timestamp = left_event.get("timeStamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    event_detail = left_event.get("eventDetail", [])
    if not event_detail or not isinstance(event_detail, list):
        return jsonify({"error": "Missing or invalid eventDetail"}), 400
    detail = event_detail[0]
    name = detail.get("name", "")
    clan = detail.get("clan", "")
    stats = left_event.get("stats", [])
    if not stats or not isinstance(stats, list):
        return jsonify({"error": "Missing or invalid stats"}), 400
    stat = stats[0]
    lastAtLoc = stat.get("lastAtLoc", "")
    levelname = stat.get("levelname", "")
    new_data = {
        "timestamp": timestamp,
        "name": name,
        "clan": clan,
        "lastAtLoc": lastAtLoc,
        "levelname": levelname
    }
    append_data_to_csv(LEFT_CSV_FILE, new_data)
    return jsonify({"message": "Left event processed", "data": payload}), 200

#####################
# GET Endpoints (Optional)
#####################

@app.route('/api/get_death_events', methods=['GET'])
def get_death_events():
    api_key_check = check_api_key()
    if api_key_check:
        return api_key_check
    try:
        df = read_csv_file(DEATH_CSV_FILE)
        return jsonify({"message": "Death events retrieved successfully", "data": df.to_dict(orient='records')}), 200
    except Exception as e:
        return jsonify({"error": f"Error retrieving death events: {e}"}), 500

@app.route('/api/get_killer_events', methods=['GET'])
def get_killer_events():
    api_key_check = check_api_key()
    if api_key_check:
        return api_key_check
    try:
        df = read_csv_file(KILLER_CSV_FILE)
        return jsonify({"message": "Killer events retrieved successfully", "data": df.to_dict(orient='records')}), 200
    except Exception as e:
        return jsonify({"error": f"Error retrieving killer events: {e}"}), 500

@app.route('/api/get_teamkill_events', methods=['GET'])
def get_teamkill_events():
    api_key_check = check_api_key()
    if api_key_check:
        return api_key_check
    try:
        df = read_csv_file(TEAMKILL_CSV_FILE)
        return jsonify({"message": "Teamkill events retrieved successfully", "data": df.to_dict(orient='records')}), 200
    except Exception as e:
        return jsonify({"error": f"Error retrieving teamkill events: {e}"}), 500

@app.route('/api/get_kys_events', methods=['GET'])
def get_kys_events():
    api_key_check = check_api_key()
    if api_key_check:
        return api_key_check
    try:
        df = read_csv_file(KYS_CSV_FILE)
        return jsonify({"message": "KYS events retrieved successfully", "data": df.to_dict(orient='records')}), 200
    except Exception as e:
        return jsonify({"error": f"Error retrieving KYS events: {e}"}), 500

@app.route('/api/get_join_events', methods=['GET'])
def get_join_events():
    api_key_check = check_api_key()
    if api_key_check:
        return api_key_check
    try:
        df = read_csv_file(JOIN_CSV_FILE)
        return jsonify({"message": "Join events retrieved successfully", "data": df.to_dict(orient='records')}), 200
    except Exception as e:
        return jsonify({"error": f"Error retrieving join events: {e}"}), 500

@app.route('/api/get_left_events', methods=['GET'])
def get_left_events():
    api_key_check = check_api_key()
    if api_key_check:
        return api_key_check
    try:
        df = read_csv_file(LEFT_CSV_FILE)
        return jsonify({"message": "Left events retrieved successfully", "data": df.to_dict(orient='records')}), 200
    except Exception as e:
        return jsonify({"error": f"Error retrieving left events: {e}"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
