from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls.exceptions import NoReverseMatch
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from synchro.models import Group, User
from synchro.serializers import GroupSerializer, UserSerializer
from rest_framework.response import Response
from django.http import JsonResponse, Http404
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def player(request, id):
    try:
        User.objects.filter(user_id=request.session['username']).get(group=id)
        return render(request, 'synchro/player.html', {
            'username': request.session['username']
        })
    except (KeyError, ObjectDoesNotExist, NoReverseMatch) as e:
        return redirect('join', id=id)


def room(request):
    return render(request, 'synchro/room.html', {'room_name_json': 'my_room'})


def home(request):
    return render(request, 'synchro/home.html')


def get_sesion_name(request):
    return JsonResponse({'username': request.session['username']})


def create_group(request):
    print(request.POST.get('username'))
    group = Group.objects.get_or_create(group_id=request.POST['groupname'])[0]
    user = User.objects.create(user_id=request.POST['username'], group=group)
    request.session['username'] = user.user_id
    return HttpResponseRedirect('player/%s' % request.POST['groupname'])


def join_room(request, id):
    return render(request, 'synchro/join.html', context={
        'group_id': id
    })


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

    # def list(self, request):
    #     queryset = Group.objects.all()
    #     serializer = GroupSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk, **kwargs):
    #     queryset = Group.objects.all()
    #     group = get_object_or_404(queryset, group_id=pk)
    #     serializer = GroupSerializer(group)
    #     return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['DELETE'])
def delete_user(request, name):
    User.objects.filter(user_id=name).delete()
    return Response(status=status.HTTP_200_OK)
