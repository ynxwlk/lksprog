from django.conf.urls import url
from . import views

from django.conf import settings

from django.contrib.auth import views as auth_views

urlpatterns = [
    #url('^login/$',views.user_login, name = "user_login" ),
    url('^login/$',auth_views.login, name = "user_login" ),
    url('^new-login/$',auth_views.login, {"template_name": "account/login.html" }),
    url('^plan/$',auth_views.login, {"template_name": "account/login.html" }),
    # url('^logout/$',auth_views.logout, name = "user_logout"),
    url('^logout/$',auth_views.logout, {"template_name": "account/logout.html" },name = 'user_logout'),
    # url(r'^register/$', views.register, name="user_register"),
]
