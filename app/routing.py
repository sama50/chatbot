from django.urls import path
from app.consumers import FileShareConsumer

websocket_urlpatterns =[
    path('ws/wsc/',FileShareConsumer.as_asgi())
]