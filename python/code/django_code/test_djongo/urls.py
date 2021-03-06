from django.urls import path
from django.urls import re_path
from test_djongo import  views


urlpatterns = [

    path('mysql-add-publish/',views.mysql_add_publish),
    path('mysql-add-author/',views.mysql_add_author),
    path('mysql-add-book/',views.mysql_add_book),
    path('registered/',views.registered, name='reg'),
    path('',views.login),
    path('query/',views.query),
    path('curl/',views.Curl),
    path('add/',views.Add),
    path('reg/',views.reg),
    path('check/',views.check),
    path('calculate/',views.calculate),
    path('auth/',views.auth)


]