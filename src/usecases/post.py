from typing import List

from src.domain.entities.post import PostEntity
from src.domain.exceptions import EntityDoesNotExist
from src.domain.services.everyone import create_uuid_int, check_permission_post


class PostInteractor:

    def __init__(self, post_repo: object):
        self.post_repo = post_repo

    def get(self, public_id, **kwargs) -> PostEntity:
        user = kwargs.pop('author')
        post = self.post_repo.get(public_id=public_id, **kwargs)

        check_permission_post(post, user)
        return post

    def all(self, **kwargs) -> List[PostEntity]:
        user = kwargs.pop('author')

        post_list = []
        posts = self.post_repo.all()

        for index, post in enumerate(posts):
            check_permission_post(post, user)
            post_list.append(post)

        if post_list:
            return post_list

        # Нужно изменить исключение на не прошёл проверку
        raise EntityDoesNotExist(message='Post is not active and does not belong to the user.')

    def create(self, **kwargs: dict) -> PostEntity:
        attempts = 5
        public_id = create_uuid_int()

        for i in range(attempts):
            try:
                return self.post_repo.create(public_id=public_id, **kwargs)
            except Exception as err:
                error = err

        raise error

    def update(self, post_id, **kwargs: dict) -> PostEntity:
        return self.post_repo.update(post_id, **kwargs)

    def delete(self, post_id: int):
        self.post_repo.delete(post_id)
