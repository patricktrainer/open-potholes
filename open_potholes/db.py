import json
import sqlite_utils
from open_potholes.handler import GitHandler


def create_tables(db):
    print("Creating tables")
    db["potholes"].create(
        {
            "id": str,
            "when": str,
            "service_request": str,
            "request_type": str,
            "request_reason": str,
            "date_created": str,
            "date_modified": str,
            "request_status": str,
            "final_address": str,
            "latitude": str,
            "longitude": str,
        },
    )


def save_pothole(db, pothole, when, hash):

    db["potholes"].insert(
        {
            "id": hash,
            "when": when,
            "latitude": pothole.get("latitude", ""),
            "longitude": pothole.get("longitude", ""),
            "service_request": pothole.get("service_request", ""),
            "request_type": pothole.get("request_type", ""),
            "request_reason": pothole.get("request_reason", ""),
            "date_created": pothole.get("date_created", ""),
            "date_modified": pothole.get("date_modified", ""),
            "request_status": pothole.get("request_status", ""),
            "final_address": pothole.get("final_address", ""),
        },
    )


def create_db(github: GitHandler):

    db = sqlite_utils.Database("potholes.db")
    if not db.tables:
        print("Creating tables")
        create_tables(db)

    it = github.parse_revisions("~/github/open-potholes", "potholes.json")

    for i, (when, hash, potholes) in enumerate(it):
        try:
            for pothole in json.loads(potholes):
                save_pothole(db, pothole, when, hash)
        except json.decoder.JSONDecodeError as e:
            print("JSONDecodeError", e)
            continue
