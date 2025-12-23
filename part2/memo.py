class InMemoryRepository:
    def __init__(self):
        self.db = {}

    def add(self, obj):
        self.db[obj.id] = obj
        return obj

    def get(self, obj_id):
        return self.db.get(obj_id)

    def list_all(self):
        return list(self.db.values())

    def update(self, obj_id, data: dict):
        obj = self.db.get(obj_id)
        if not obj:
            return None
        for key, value in data.items():
            setattr(obj, key, value)
        obj.update_timestamp()
        return obj

    def delete(self, obj_id):
        return self.db.pop(obj_id, None)
