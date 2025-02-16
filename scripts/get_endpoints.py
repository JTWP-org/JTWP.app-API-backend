from flask import Blueprint, jsonify
import pandas as pd
import json

# Load configuration for CSV file paths
with open("config.json", "r") as f:
    config = json.load(f)
csv_paths = config["CSV_FILE_PATHS"]

get_bp = Blueprint("get_bp", __name__)

def read_csv_file(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return pd.DataFrame()

@get_bp.route("/api/get_death_events", methods=["GET"])
def get_death_events():
    df = read_csv_file(csv_paths["DEATH_CSV_FILE"])
    return jsonify({"message": "Death events retrieved successfully", "data": df.to_dict(orient="records")}), 200

@get_bp.route("/api/get_killer_events", methods=["GET"])
def get_killer_events():
    df = read_csv_file(csv_paths["KILLER_CSV_FILE"])
    return jsonify({"message": "Killer events retrieved successfully", "data": df.to_dict(orient="records")}), 200

@get_bp.route("/api/get_teamkill_events", methods=["GET"])
def get_teamkill_events():
    df = read_csv_file(csv_paths["TEAMKILL_CSV_FILE"])
    return jsonify({"message": "Teamkill events retrieved successfully", "data": df.to_dict(orient="records")}), 200

@get_bp.route("/api/get_kys_events", methods=["GET"])
def get_kys_events():
    df = read_csv_file(csv_paths["KYS_CSV_FILE"])
    return jsonify({"message": "KYS events retrieved successfully", "data": df.to_dict(orient="records")}), 200

@get_bp.route("/api/get_join_events", methods=["GET"])
def get_join_events():
    df = read_csv_file(csv_paths["JOIN_CSV_FILE"])
    return jsonify({"message": "Join events retrieved successfully", "data": df.to_dict(orient="records")}), 200

@get_bp.route("/api/get_left_events", methods=["GET"])
def get_left_events():
    df = read_csv_file(csv_paths["LEFT_CSV_FILE"])
    return jsonify({"message": "Left events retrieved successfully", "data": df.to_dict(orient="records")}), 200
