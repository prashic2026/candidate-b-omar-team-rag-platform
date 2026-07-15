from src.acl import filter_by_acl

def search(records, allowed_ids, query):
    visible = filter_by_acl(records, allowed_ids)
    return [r for r in visible if query.lower() in r.get("text","").lower()]
