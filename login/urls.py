from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="loginmain"),
    path("login/",views.login,name="login"),   
]
