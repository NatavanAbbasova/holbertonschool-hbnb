from persistence.in_memory_repo import InMemoryRepository
from business.models.user import User
from business.models.amenity import Amenity
from business.models.place import Place
from business.models.review import Review

class HBnBFacade:
    def __init__(self):
        self.users = InMemoryRepository()
        self.amenities = InMemoryRepository()
        self.places = InMemoryRepository()
        self.reviews = InMemoryRepository()

    # USER
    def create_user(self, data):
        user = User(**data)
        return self.users.add(user)

    def list_users(self):
        return self.users.list_all()

    def get_user(self, user_id):
        return self.users.get(user_id)

    def update_user(self, user_id, data):
        return self.users.update(user_id, data)
