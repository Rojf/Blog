from typing import List

from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from src.domain.entities.comment import CommentEntity


class Comment(models.Model):
    public_id = models.PositiveIntegerField()

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]

    def __str__(self) -> str:
        return f"{self.author} - {self.public_id}"

    def map(self, fields: List[str] = None) -> CommentEntity:
        fields = fields or [str(field) for field in CommentEntity.__dataclass_fields__]
        attrs = {field: getattr(self, field) for field in fields}
        return CommentEntity(**attrs)