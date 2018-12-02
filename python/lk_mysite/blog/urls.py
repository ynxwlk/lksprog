# from django.urls import path
from django.conf.urls import url
from . import views
# from django.contrib import admin
# app_name='blog'
urlpatterns = [
    url(r'^$', views.blog_title, name = "blog_title"),
    url(r'(?P<article_id>\d)/$', views.blog_article, name = "blog_detail")
    # path('$', views.blog_title, name = "blog_title"),
    # path('int:article_id',views.blog_article, name = "blog_detail")
]
