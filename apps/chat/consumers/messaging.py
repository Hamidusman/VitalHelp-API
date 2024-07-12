import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class MessageConsumer(WebsocketConsumer):
    def new_call(self, event):
        message = event['message']
        self.send(text_data=json({'message': message,
                                 'status': 'new call'}
                                 ))
    def end_call(self, event):
        message = event['message']
        self.send(text_data=json({'message': message,
                                 'status': 'end call'}
                                 ))
###    def disconnect(self, code):
###        async_to_sync(self.channel_layer.group_discard)()