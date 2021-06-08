from django.urls import path
from . import views
from .feeds import LatestPostFeed

app_name = 'blog'

urlpatterns=[
        path('category/', views.category, name='category'),
        path('test/', views.test, name='test'),
        path('', views.post_list, name='post_list'),
        path('contact.html', views.contact, name='contact'),
        # path('', views.PostListView.as_view(), name='post_list'),
        path('tag/<slug:tag_slug>', views.tagss, name='post_list_by_tag'),
        path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
        path('<int:post_id>/share/', views.post_share, name='post_share'),
        path('feed/', LatestPostFeed(), name='post_feed'),
        path('blog_search', views.blog_search, name='blog-search'),
    ]