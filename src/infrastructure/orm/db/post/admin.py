from django.contrib import admin

from src.infrastructure.adminsite.post.admin import PostAdmin
from src.infrastructure.orm.db.post.models import Post


admin.site.register(Post, PostAdmin)
