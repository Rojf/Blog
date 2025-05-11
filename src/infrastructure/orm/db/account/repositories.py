from django.db.utils import IntegrityError

from src.domain.exceptions import EntityDoesNotExist, EntityDuplicate
from src.domain.entities.account import UserEntity


class UserDatabaseRepository:

    def get(self) -> UserEntity:
        pass

    def all(self) -> UserEntity:
        pass

    def filter(self, *args, **kwargs) -> UserEntity:
        pass

    def create(self) -> UserEntity:
        pass
    
    def update(self) -> UserEntity:
        pass
    
    def delete(self):
        pass
        