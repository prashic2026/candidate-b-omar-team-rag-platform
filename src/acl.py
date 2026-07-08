def filter_by_acl(records, allowed_ids):
    allowed = set(allowed_ids)
    return [r for r in records if r.get("id") in allowed]
