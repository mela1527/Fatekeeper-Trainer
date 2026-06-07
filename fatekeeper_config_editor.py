#!/usr/bin/env python3
"""
Fatekeeper Config Editor - Edit save file or configs to change resources.
"""

import os
import json
import shutil
from datetime import datetime

CONFIG_PATH = os.path.expandvars(r"%APPDATA%\Fatekeeper\saves\config.json")
BACKUP_DIR = os.path.expanduser("~/FatekeeperBackups")

def backup_config():
    if not os.path.exists(CONFIG_PATH):
        print("Config not found.")
        return False
    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_DIR, f"config_{timestamp}.json")
    shutil.copy2(CONFIG_PATH, backup_file)
    print(f"Backup saved: {backup_file}")
    return True

def edit_resources():
    if not os.path.exists(CONFIG_PATH):
        print("Config file missing.")
        return
    with open(CONFIG_PATH, 'r') as f:
        data = json.load(f)
    # Modify values (example)
    data['resources']['gold'] = 99999
    data['skill_points'] = 100
    with open(CONFIG_PATH, 'w') as f:
        json.dump(data, f, indent=2)
    print("Resources updated!")

if __name__ == "__main__":
    backup_config()
    edit_resources()
    print("Done. Launch Fatekeeper.")