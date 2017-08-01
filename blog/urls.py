from django.conf.urls import include, url
from . import views


urlpatterns = [

    url(r'^blog/blog_list/$', views.blog_list, name='blog_list'),
    ]