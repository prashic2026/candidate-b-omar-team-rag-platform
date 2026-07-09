from src.acl import filter_by_acl

def test_acl_filter():
    records = [{"id":"1"},{"id":"2"}]
    assert filter_by_acl(records, ["2"]) == [{"id":"2"}]
