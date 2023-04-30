import os

from tinydb import TinyDB, Query


# Peer_id: 123
# Allow sending: True, False
class Database:
    def __init__(self, name='db.json'):
        self.db = TinyDB(os.path.join(os.getcwd(), name))

    async def update(self, data):
        return self.db.update(data)

    async def remove(self, data):
        return self.db.remove(data)

    async def all(self):
        return self.db.all()

    async def search(self, data):
        return self.db.search(data)

    async def insert(self, data):
        return self.db.insert(data)
