from channels.routing import ProtocolTypeRouter , URLRouter
from channels.auth import AuthMiddlewareStack
from hyk.middlewares.channels_middlewares.token_auth import Channels_Token_Auth
from hyk.information import routing
from django.urls import path

application = ProtocolTypeRouter({
    'websocket':
        Channels_Token_Auth(
        URLRouter(
       routing.websocket_urlpatterns
            
        ),
       
    ),
})