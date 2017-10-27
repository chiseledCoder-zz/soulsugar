from django.conf.urls import include, url
from . import views


urlpatterns = [

    url(r'^blog/blog_list/$', views.blog_list, name='blog_list'),
    url(r'^blog/tag_search/(?P<tag_name>[\w-]+)$', views.tag_search, name='tag_search'),
    url(r'^blog/category_search/(?P<category_name>[\w-]+)$', views.category_search, name='category_search'),
    ]