from typing import List

from django.db.utils import IntegrityError

from src.infrastructure.orm.db.post.models import Post
from src.domain.exceptions import EntityDoesNotExist, EntityDuplicate
from src.domain.entities.post import PostEntity


class PostDatabaseRepository:

    @staticmethod
    def get(**kwargs) -> PostEntity:
        try:
            post = Post.objects.get(**kwargs)
        except Post.DoesNotExist:
            raise EntityDoesNotExist(message=f"Post does not exist with this public_id no.{kwargs.get('public_id')}")

        return post.map()

    @staticmethod
    def all() -> List[PostEntity]:
        posts = Post.objects.all()

        return [post.map() for post in posts]

    @staticmethod
    def create(**kwargs: dict) -> PostEntity:
        tags = kwargs.pop('tags', [])

        try:
            post = Post.objects.create(**kwargs)

            if tags:
                post.tags.set(tags)
                post.save()

        except IntegrityError:
            raise EntityDuplicate(message="Already exists a post with this data.")

        return post.map()

    @staticmethod
    def update(public_id, **kwargs) -> PostEntity:
        try:
            instance = Post.objects.get(public_id=public_id)
        except Post.DoesNotExist:
            raise EntityDoesNotExist(message=f"Post does not exist with this public_id no.{public_id}")
        tags = kwargs.pop('tags', [])

        for key, value in kwargs.items():
            setattr(instance, key, value)

        if tags:
            instance.tags.set(tags)

        instance.save()

        return instance.map()

    @staticmethod
    def delete(public_id: int):
        try:
            instance = Post.objects.get(public_id=public_id)
        except Post.DoesNotExist:
            raise EntityDoesNotExist(message=f"Post does not exist with this public_id no.{public_id}")

        instance.delete()
