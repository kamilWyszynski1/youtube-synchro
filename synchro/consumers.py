from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from synchro.models import Connection


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'room'
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name)

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        Connection.objects.filter(user_id=self.room_name).delete()
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(self.room_group_name, {'type': 'chat_message', 'message': message})

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({'message': message}))

class VideoConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['id']
        self.room_group_name = 'player_%s' % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,self.channel_name)

        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        pause = text_data_json['pause']
        seconds = text_data_json['seconds']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                'type': 'chat_message',
                'pause': pause,
                'seconds': seconds
            }
        )

    def chat_message(self, event):
        pause = event['pause']
        seconds = event['seconds']

        self.send(text_data=json.dumps({
            'pause': pause,
            'seconds': seconds
        }))

