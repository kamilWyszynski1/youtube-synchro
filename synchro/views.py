from django.shortcuts import render, HttpResponseRedirect
from synchro.serializers import ConnectionSerializer
from synchro.models import Connection
from rest_framework import viewsets, generics


# Create your views here.


def player(request, id):
    return render(request, 'synchro/player.html', {})


def room(request):
    return render(request, 'synchro/room.html', {'room_name_json': 'my_room'})


def home(request):
    return render(request, 'synchro/home.html')


def createGroup(request):
    Connection.objects.create(user_id=request.POST['username'], room_id=request.POST['groupname'])
    return HttpResponseRedirect('player/%s' % request.POST['groupname'])


class ConnectionViewSet(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer


class RoomViewSet(generics.ListAPIView):
    serializer_class = ConnectionSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Connection.objects.filter(room_id=id)
