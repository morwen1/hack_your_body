#rest framework
import datetime

from rest_framework import serializers


#serializers
#from hyk.users.serializers import ProfileSerializerListExtra
from hyk.exercises.serializers import RutineSerializerList ,ProfileSerializerListExtra

#models
from hyk.exercises.models import Sessions
from hyk.users.models import Profile
from hyk.information.models import Info_Sessions






"""
Serializers for the sessions
profile -> sessions
sessions --> profile
sessions --> rutine
sessions --> info_session 
"""

class SessionsSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Sessions
        fields =('id'  ,'session_rutines' , 'duration')

    def create(self , validate_data):
        info_session = Info_Sessions.objects.create(time = datetime.time())
        info_session.save()
        profile = Profile.objects.get(user=self.context['request'].user)
        session =Sessions.objects.create(
            session_profile = profile , 
            session_rutines=validate_data['session_rutines'],
            duration = validate_data['duration'],
            info_session = info_session,
            )
        session.save()
        return session


class SessionsSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Sessions
        fields =('duration' ,'session_rutines')


class SessionsSerializer(serializers.ModelSerializer):
    session_profile = ProfileSerializerListExtra(read_only=True)
    session_rutines = RutineSerializerList(read_only=True)
    class Meta:
        model = Sessions
        fields =(
            'id' , 
            'session_profile' ,
            'session_rutines' , 
            'duration',
            'created',
            )