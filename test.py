import os, json

base_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(base_dir, "subsets.json")
if not os.path.exists(json_path):
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({}, f, indent=4)