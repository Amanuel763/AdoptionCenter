from turtle import home
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),

]
