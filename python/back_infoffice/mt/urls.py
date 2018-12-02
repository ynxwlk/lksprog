from django.urls import path
# from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.mt_sqdw, name = 'mt_sqdw'),
    # url(r'^$', views.mt_sqdw,name="mt_sqdw"),
]