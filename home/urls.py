from django.contrib import admin
from . import views
from django.urls import path,include

urlpatterns = [
    path("", views.signup, name='signup'),
    path("signin", views.signin, name='signin'),
    path("logout", views.logout, name='logout'),
    path("index", views.index, name='index'),
]
