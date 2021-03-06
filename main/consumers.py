from channels.generic.websocket import AsyncWebsocketConsumer
import json


class MainConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'main_quiz'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'main_message',
                'message': message
            }
        )

    async def main_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message' : message
        }))