import json
from channels.generic.websocket import AsyncWebsocketConsumer 
from asgiref.sync import async_to_sync
from time import sleep
import openai ,os


aip_key= 'YOUR_KEY'

class FileShareConsumer(AsyncWebsocketConsumer):
    count_root =0
    async def connect(self):
        print("==================")
        await self.accept()
         
        # ChatConsumer.count = ChatConsumer.count +1
        await self.send(text_data=json.dumps({
            'message': "Hello! How can I help you today?"
        }))
         
         
    
    async def disconnect(self, close_code):
         
        await self.disconnect()

    async def receive(self, text_data):
        print(text_data)
        openai.api_key = aip_key
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=text_data,
            max_tokens=256,
            temperature=0.5
        )
        actual_ress = json.dumps(response['choices'])
        actual_ress = json.loads(actual_ress)
       
        res = actual_ress[0]['text']
        await self.send(text_data=json.dumps({
            'message': res
        }))
    