from django.urls import path
from . import views

urlpatterns = [
    path('', views.adopt, name='adopt'),
    path('search', views.search, name='search'),
]
