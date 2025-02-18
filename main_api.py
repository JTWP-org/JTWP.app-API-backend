from flask import Flask, request, jsonify, send_file
from datetime import datetime
import os, json, pandas as pd

# Import modules from the scripts folder
from scripts.api_key import check_api_key
from scripts.get_endpoints import get_bp
from scripts.csv_init import initialize_all_csvs

# Load configuration for CSV file paths from config.json
with open("config.json", "r") as f:
    config = json.load(f)
csv_paths = config["CSV_FILE_PATHS"]

app = Flask(__name__)
app.register_blueprint(get_bp)

# Initialize CSV files at startup
initialize_all_csvs()

def read_csv_file(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return pd.DataFrame()

def append_data_to_csv(file_path, new_data):
    try:
        df = read_csv_file(file_path)
        new_df = pd.DataFrame([new_data])
        df = pd.concat([df, new_df], ignore_index=True)
        df.to_csv(file_path, index=False)
        print(f"Data added to {file_path}.")
    except Exception as e:
        print(f"Error appending data to {file_path}: {e}")

############################
# POST Endpoints
############################

# POST endpoint for death events
@app.route('/api/submit_death', methods=['POST'])
def submit_death():
    if not check_api_key(request):
        return jsonify({"error": "Unauthorized access. Invalid API key."}), 401
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
    append_data_to_csv(csv_paths["DEATH_CSV_FILE"], new_data)
    return jsonify({"message": "Death event processed", "data": payload}), 200

# POST endpoint for killer events
@app.route('/api/submit_killer', methods=['POST'])
def submit_killer():
    if not check_api_key(request):
        return jsonify({"error": "Unauthorized access. Invalid API key."}), 401
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
    append_data_to_csv(csv_paths["KILLER_CSV_FILE"], new_data)
    return jsonify({"message": "Killer event processed", "data": payload}), 200

# POST endpoint for teamkill events
@app.route('/api/submit_teamkill', methods=['POST'])
def submit_teamkill():
    if not check_api_key(request):
        return jsonify({"error": "Unauthorized access. Invalid API key."}), 401
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
    append_data_to_csv(csv_paths["TEAMKILL_CSV_FILE"], new_data)
    return jsonify({"message": "Teamkill event processed", "data": payload}), 200

# POST endpoint for KYS events
@app.route('/api/submit_kys', methods=['POST'])
def submit_kys():
    if not check_api_key(request):
        return jsonify({"error": "Unauthorized access. Invalid API key."}), 401
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
    append_data_to_csv(csv_paths["KYS_CSV_FILE"], new_data)
    return jsonify({"message": "KYS event processed", "data": payload}), 200

# POST endpoint for join events
@app.route('/api/submit_join', methods=['POST'])
def submit_join():
    if not check_api_key(request):
        return jsonify({"error": "Unauthorized access. Invalid API key."}), 401
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
    append_data_to_csv(csv_paths["JOIN_CSV_FILE"], new_data)
    return jsonify({"message": "Join event processed", "data": payload}), 200

# POST endpoint for left events
@app.route('/api/submit_left', methods=['POST'])
def submit_left():
    if not check_api_key(request):
        return jsonify({"error": "Unauthorized access. Invalid API key."}), 401
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
    append_data_to_csv(csv_paths["LEFT_CSV_FILE"], new_data)
    return jsonify({"message": "Left event processed", "data": payload}), 200

############################
# NEW ENDPOINT: Serve Player Stats JSON for Website
############################

@app.route('/api/player_stats', methods=['GET'])
def get_player_stats():
    # Path to the JSON file with player stats
    json_file_path = "/home/steam/api2/JTWP.app-API-backend/math/tempOut/player_stats.json"
    try:
        return send_file(json_file_path, mimetype='application/json')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

############################
# GET Endpoints (Optional)
############################

# New endpoint to count items from killer events (ignoring death items)
@app.route('/api/item_stats', methods=['GET'])
def item_stats():
    if not check_api_key(request):
        return jsonify({"error": "Unauthorized access. Invalid API key."}), 401
    try:
        # Read the killer events CSV file (assuming items from killer events are recorded there)
        df = pd.read_csv(csv_paths["KILLER_CSV_FILE"])
        # Clean the "item" column and count occurrences (ignoring empty entries)
        if "item" not in df.columns:
            return jsonify({"error": "'item' column not found in killer events data"}), 400
        # Remove any leading/trailing whitespace, then count occurrences
        df["item"] = df["item"].astype(str).str.strip()
        item_counts = df["item"].value_counts().to_dict()
        return jsonify({
            "message": "Item stats retrieved successfully",
            "data": item_counts
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/get_death_events', methods=['GET'])
def get_death_events():
    if not check_api_key(request):
        return jsonify({"error": "Unauthorized access. Invalid API key."}), 401
    try:
        df = read_csv_file(csv_paths["DEATH_CSV_FILE"])
        return jsonify({"message": "Death events retrieved successfully", "data": df.to_dict(orient='records')}), 200
    except Exception as e:
        return jsonify({"error": f"Error retrieving death events: {e}"}), 500

@app.route('/api/get_killer_events', methods=['GET'])
def get_killer_events():
    if not check_api_key(request):
        return jsonify({"error": "Unauthorized access. Invalid API key."}), 401
    try:
        df = read_csv_file(csv_paths["KILLER_CSV_FILE"])
        return jsonify({"message": "Killer events retrieved successfully", "data": df.to_dict(orient='records')}), 200
    except Exception as e:
        return jsonify({"error": f"Error retrieving killer events: {e}"}), 500

@app.route('/api/get_teamkill_events', methods=['GET'])
def get_teamkill_events():
    if not check_api_key(request):
        return jsonify({"error": "Unauthorized access. Invalid API key."}), 401
    try:
        df = read_csv_file(csv_paths["TEAMKILL_CSV_FILE"])
        return jsonify({"message": "Teamkill events retrieved successfully", "data": df.to_dict(orient='records')}), 200
    except Exception as e:
        return jsonify({"error": f"Error retrieving teamkill events: {e}"}), 500

@app.route('/api/get_kys_events', methods=['GET'])
def get_kys_events():
    if not check_api_key(request):
        return jsonify({"error": "Unauthorized access. Invalid API key."}), 401
    try:
        df = read_csv_file(csv_paths["KYS_CSV_FILE"])
        return jsonify({"message": "KYS events retrieved successfully", "data": df.to_dict(orient='records')}), 200
    except Exception as e:
        return jsonify({"error": f"Error retrieving KYS events: {e}"}), 500

@app.route('/api/get_join_events', methods=['GET'])
def get_join_events():
    if not check_api_key(request):
        return jsonify({"error": "Unauthorized access. Invalid API key."}), 401
    try:
        df = read_csv_file(csv_paths["JOIN_CSV_FILE"])
        return jsonify({"message": "Join events retrieved successfully", "data": df.to_dict(orient='records')}), 200
    except Exception as e:
        return jsonify({"error": f"Error retrieving join events: {e}"}), 500

@app.route('/api/get_left_events', methods=['GET'])
def get_left_events():
    if not check_api_key(request):
        return jsonify({"error": "Unauthorized access. Invalid API key."}), 401
    try:
        df = read_csv_file(csv_paths["LEFT_CSV_FILE"])
        return jsonify({"message": "Left events retrieved successfully", "data": df.to_dict(orient='records')}), 200
    except Exception as e:
        return jsonify({"error": f"Error retrieving left events: {e}"}), 500

@app.route('/player_stats.json', methods=['GET'])
def player_stats():
    json_file_path = "/home/steam/api2/JTWP.app-API-backend/math/tempOut/player_stats.json"
    try:
        return send_file(json_file_path, mimetype='application/json')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

