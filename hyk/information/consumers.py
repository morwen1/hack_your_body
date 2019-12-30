from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from hyk.exercises.models import Sessions
from hyk.users.models import Profile
from hyk.information.models import Info_Sessions
from hyk.information.serializers.info_sessions import Info_sessions_Serializer
from django.db.models import Q
import json


class InformationConsumer (AsyncJsonWebsocketConsumer):
    
    
    async def connect(self):

        self.session = await self.obtain_information()
        await self.accept()
        await self.send(text_data=json.dumps(self.session))
    


    async def disconnect(self , close_code) :
        await self.close()
    


    async def receive_json(self, content, **kwargs):
        message = await self.save_information(information=self.information,content=content )
        await self.send_json(content=message.data)



    @database_sync_to_async
    def save_information(self , content , information):
        
        message = Info_sessions_Serializer(information,data=content , partial=True)
        message.is_valid(raise_exception=True)
        message.save()
        return message

    @database_sync_to_async
    def obtain_information(self):

        id_session = self.scope['url_route']['kwargs']['id_session']
        session = Sessions.objects.filter(
            Q(
                session_profile =Profile.objects.get(user=self.scope['user'])
            )&
            Q(
                id=id_session
            )
            )
        self.information = session.first().info_session

        return Info_sessions_Serializer(self.information).data