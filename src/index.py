def index_chunks(chunks, store):
    for chunk in chunks:
        store.upsert(chunk["id"], chunk["text"])
