import json
import os

# Anchor save files to this script's own folder, so they always land in the
# same place no matter where the program is launched from (double-click,
# terminal, IDE run button, etc. can all have different working directories).
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_FILE = os.path.join(BASE_DIR, "discovered_fusions.json")
HISTORY_FILE = os.path.join(BASE_DIR, "battle_history.json")

def load_discovered():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            return set(data)
    return set()

def save_discovered(discovered):
    with open(SAVE_FILE, "w") as f:
        json.dump(list(discovered), f)
    print("Progress saved!")

def load_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)