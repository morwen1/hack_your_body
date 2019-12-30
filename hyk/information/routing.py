from django.urls import re_path
from .consumers import InformationConsumer


websocket_urlpatterns= [
    re_path(r'ws/information/(?P<id_session>[0-9]+)' , InformationConsumer),
]