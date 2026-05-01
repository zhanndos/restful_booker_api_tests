import os
import json 

def load_config(file):
    """Load configuration from a JSON file."""
    
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
    with open(config_file) as f:
        return json.load(f)

config = load_config("config_file.json")

BASE_URL = config["BASE_URL"]
USER = config["USER"]
PASSWORD = config["PASSWORD"]