from django.contrib.auth import get_user_model

from blog.models import Post, Comment
from taggit.models import Tag

from .base import BaseRepository


class PostRepository(BaseRepository):
    model = Post

    @classmethod
    def published(cls):
        return cls.model.published


class TegRepository(BaseRepository):
    model = Tag


class CommentRepository(BaseRepository):
    model = Comment


class UserRepository(BaseRepository):
    model = get_user_model()
