
import json
import config

CONFIG_FILE = "config.json"

def read_config():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def write_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)
