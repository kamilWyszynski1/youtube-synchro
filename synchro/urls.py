from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('connections', views.ConnectionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('player/<int:id>', views.player, name='player'),
    path('room', views.room, name='room'),
    path('', views.home, name='home'),
    path('create-group', views.createGroup, name='create-group'),
    path('connections/<int:id>', views.RoomViewSet.as_view()),
]