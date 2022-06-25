import json

def load_data(filename) -> list[dict]:
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
        return data