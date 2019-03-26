from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('groups', views.GroupViewSet, basename='group')
router.register('users', views.UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('player/<int:id>', views.player, name='player'),
    path('player/<int:id>/join', views.join_room, name='join'),
    path('room', views.room, name='room'),
    path('', views.home, name='home'),
    path('create-group', views.create_group, name='create-group'),
    path('delete_user/<str:name>', views.delete_user),
    path('get_session', views.get_sesion_name, name='get_session'),
]