from django.conf.urls import include
from django.urls import path

from src.infrastructure.api.routes.post.routers import PostRouter
from src.infrastructure.api.views.post import PostViewSet, PostCreateViewSet, PostListViewSet


post_router = PostRouter()
post_router.register('', viewset=PostViewSet, basename='post-detail')
post_router.register('', viewset=PostListViewSet, basename='post-list')
post_router.register('', viewset=PostCreateViewSet, basename='post-create')


urlpatterns = [
    path('', include(post_router.urls)),
]

