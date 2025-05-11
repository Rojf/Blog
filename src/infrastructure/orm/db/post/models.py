from typing import List

from django.db import models
from django.utils import timezone
from django.conf import settings

from taggit.managers import TaggableManager

from src.domain.entities.post import PostEntity


class Post(models.Model):
    public_id = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=300, unique_for_date='publish')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=3000)
    tags = TaggableManager()

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    published = models.BooleanField(default=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-publish']

    def __str__(self) -> str:
        return f"{self.author} - {self.title}"

    def map(self, fields: List[str] = None) -> PostEntity:
        fields = fields or [str(field) for field in PostEntity.__dataclass_fields__]
        attrs = {field: getattr(self, field) for field in fields}
        return PostEntity(**attrs)
