import sqlite_utils
import json


def load_json(filename):
    """load the json file into a python object"""
    with open(filename) as f:
        return json.load(f)


if __name__ == "__main__":
    db = sqlite_utils.Database("311calls.db")

    calls = load_json("311calls.json")
    for call in calls:
        db["calls"].insert(call, alter=True, replace=True)
