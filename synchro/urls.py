from django.urls import path
from . import views

urlpatterns = [
    path('player/<int:id>', views.player, name='player'),
    path('room', views.room, name='room'),
    path('', views.home, name='home'),
    path('create-group', views.createGroup, name='create-group')
]