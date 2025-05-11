from src.domain.entities.post import PostEntity


class PostRepository:
    def __init__(self, db_repo: object, cache_repo: object) -> None:
        self.db_repo = db_repo
        self.cache_repo = cache_repo
    
    def get(self, **kwargs) -> PostEntity:
        post = self.cache_repo.get(**kwargs)

        if not post:
            post = self.db_repo.get(**kwargs)
            # self.cache_repo.save(public_id, post)
        
        return post

    def all(self) -> PostEntity:
        posts = self.db_repo.all()
        # for post in posts:
        #     self.cache_repo.save(post.public_id, post)

        return posts

    def create(self, **kwargs: dict) -> PostEntity:
        return self.db_repo.create(**kwargs)
    
    def update(self,**kwargs) -> PostEntity:
        return self.db_repo.update(**kwargs)

    def delete(self, public_id: int):
        return self.db_repo.delete(public_id)