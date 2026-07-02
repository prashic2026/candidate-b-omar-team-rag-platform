def normalize_record(record):
    return {"id": str(record["id"]), "text": record.get("text", "").strip()}
