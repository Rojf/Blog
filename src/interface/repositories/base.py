from typing import List

from src.domain.exceptions import EntityDoesNotExist, EntityDuplicate
from src.domain.entities.post import PostEntity


class BaseRepository:
    model = None

    @classmethod
    def get(cls, *args: list, **kwargs: dict) -> PostEntity:
        try:
            return cls.model.objects.get(*args, **kwargs).map()
        except cls.model.DoesNotExist:
            raise EntityDoesNotExist(message=f"Post does not exist with this id no.{id}")

    @classmethod
    def create(cls, **kwargs:dict) -> PostEntity:
        try:
            return cls.model.objects.create(**kwargs).map()
        except Exception as err:
            raise EntityDuplicate(message="Already exists a post with this data.")

    @classmethod
    def update(cls, *args, **kwargs) -> PostEntity:
        tags = kwargs.pop('tags', [])

        try:
            instance = cls.model.objects.get(*args, **kwargs)
        except cls.model.DoesNotExist:
            raise EntityDoesNotExist(message=f"Post does not exist with this id no.{id}")

        for key, value in kwargs.items():
            setattr(instance, key, value)

        if tags:
            instance.tags.set(tags)

        instance.save()
        return instance.map()

    @classmethod
    def delete(cls, *args, **kwargs):
        try:
            instance = cls.model.objects.get(*args, **kwargs)
        except cls.model.DoesNotExist:
            raise EntityDoesNotExist(message=f"Post does not exist with this id no.{id}")

        instance.delete()

    @classmethod
    def all(cls, *args, **kwargs) -> List[PostEntity]:
        return [post.map() for post in cls.model.objects.all(*args, **kwargs)]
