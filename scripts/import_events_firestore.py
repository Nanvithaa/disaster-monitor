import json
from datetime import timezone

from dateutil import parser as dtparser
from google.cloud import firestore


def to_firestore_dt(iso_str: str):
    """
    Convert ISO string like '2020-10-25T00:05:32Z' to timezone-aware datetime.
    Firestore Python client stores datetime as a Timestamp automatically.
    """
    dt = dtparser.parse(iso_str)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    else:
        dt = dt.astimezone(timezone.utc)
    return dt


def main():
    db = firestore.Client()

    with open("events.json", "r", encoding="utf-8") as f:
        events = json.load(f)

    for ev in events:
        ev = dict(ev)  # copy

        # Convert to Firestore Timestamp fields
        ev["start_time"] = to_firestore_dt(ev["start_time"])
        ev["end_time"] = to_firestore_dt(ev["end_time"])
        ev["updated_at"] = firestore.SERVER_TIMESTAMP

        event_id = ev["eventId"]
        db.collection("events").document(event_id).set(ev, merge=True)
        print("Upserted:", event_id)


if __name__ == "__main__":
    main()

