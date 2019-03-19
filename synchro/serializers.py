from synchro.models import  Group, User
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    users = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='user_id'
    )

    class Meta:
        model = Group
        fields = ('group_id', 'users')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'user_id', 'group')
