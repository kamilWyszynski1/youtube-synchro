from synchro.models import Connection
from rest_framework import serializers


class ConnectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Connection
        lookup_field = 'room_id'
        fields = ('user_id', 'room_id')
        extra_kwargs = {'url': {'lookup_field': 'room_id'}}

