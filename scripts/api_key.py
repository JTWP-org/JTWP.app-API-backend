import os
import json
from dotenv import load_dotenv

# Load configuration to get the API_KEY_PATH
with open("config.json", "r") as f:
    config = json.load(f)

api_key_path = config.get("API_KEY_PATH", ".env")
load_dotenv(api_key_path)

API_KEY = os.getenv("API_KEY")

def check_api_key(request):
    provided_key = request.headers.get("X-API-Key")
    return provided_key == API_KEY
