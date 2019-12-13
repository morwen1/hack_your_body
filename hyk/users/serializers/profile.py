#django 

#rest_framework 
from rest_framework import serializers
#user serializer
from hyk.users.serializers import UserSerializer
#models
from hyk.users.models import Profile



class ProfileSerializer (serializers.ModelSerializer):
    user = UserSerializer(read_only =True , many = False)
    class Meta:
        model = Profile
        fields = ('__all__')


class ProfileSerializerCreate (serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'weigth',
            'height',
            'imc',
            'atlhetic_discipline'
        )