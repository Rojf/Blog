from src.infrastructure.orm.db.account.repositories import UserDatabaseRepository
from src.interface.controllers.account import UserController
from src.interface.repositories.account import UserRepository
from src.usecases.account import UserInteractor


class UserDatabaseRepositoryFactory:

    @staticmethod
    def get() -> UserDatabaseRepository:
        return UserDatabaseRepository()


class UserRepositoryFactory:

    @staticmethod
    def get() -> UserRepository:
        db_repo = UserDatabaseRepositoryFactory.get()
        return UserRepository(db_repo)


class UserInteractorFactory:

    @staticmethod
    def get() -> UserInteractor:
        post_repo = UserRepositoryFactory.get()
        
        return UserInteractor(post_repo)
    

class UserViewSetFactory:

    @staticmethod
    def create() -> UserController:
        user_interactor = UserInteractorFactory.get()
        return UserController(user_interactor)
