from django.conf.urls import url

from synchro import consumers


websocket_urlpatterns = [
    url('ws/chat/', consumers.ChatConsumer),
    url('ws/video/(?P<id>[-\w]+)/$', consumers.VideoConsumer),
]