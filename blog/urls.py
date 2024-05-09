from django.urls import path

from blog import views
from blog.feeds import LatesPostsFeed


app_name = 'blog'

urlpatterns = [
    # path('', views.PostListView.as_view(), name='post_list'),
    path('', views.post_list_view, name='post_list'),
    path('tag/<str:tag_slug>/', views.post_list_view, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    path('feed/', LatesPostsFeed(), name='post_feed'),
    path('<int:post_id>/like/', views.post_like, name='post_like'),
    path('search/', views.post_search, name='post_search'),
]
