from django.urls import path, include
from . import views
 
urlpatterns = [
    path('sb/', views.mt_shengbao),
    #path('bz/', views.banzheng),
    #path('dbdw/', views.dbdw),
    # url(r'^$', 'mt.views.home', name='home'),
]
