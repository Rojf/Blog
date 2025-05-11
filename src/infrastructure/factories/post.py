# from src.infrastructure.orm.cache.post_rate.repositories import PostCacheRepository
from src.infrastructure.orm.db.post.repositories import PostDatabaseRepository
from src.interface.controllers.post import PostController
from src.interface.repositories.post import PostRepository
from src.usecases.post import PostInteractor


class PostDatabaseRepositoryFactory:

    @staticmethod
    def get() -> PostDatabaseRepository:
        return PostDatabaseRepository()
    

class PostCacheRepositoryFactory:

    # @staticmethod
    # def get() -> PostCacheRepository:
    #     return PostCacheRepository()

    @staticmethod
    def get() -> PostDatabaseRepository:
        return PostDatabaseRepository()


class PostRepositoryFactory:

    @staticmethod
    def get() -> PostRepository:
        db_repo = PostDatabaseRepositoryFactory.get()
        cache_repo = PostCacheRepositoryFactory.get()
        return PostRepository(db_repo, cache_repo)


class PostInteractorFactory:

    @staticmethod
    def get() -> PostInteractor:
        post_repo = PostRepositoryFactory.get()
        
        return PostInteractor(post_repo)
    

class PostViewSetFactory:

    @staticmethod
    def create() -> PostController:
        user_interactor = PostInteractorFactory.get()
        return PostController(user_interactor)
