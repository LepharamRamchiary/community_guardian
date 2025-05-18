import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.me = self.scope['user']
        self.friend = self.scope['url_route']['kwargs']['username']
        self.room_name = f"chat_{min(self.me.username, self.friend)}_{max(self.me.username, self.friend)}"
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        sender = self.scope['user']
        receiver = User.objects.get(username=self.friend)

        msg = Message.objects.create(sender=sender, receiver=receiver, content=message)

        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender.username
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender']
        }))