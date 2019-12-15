#django 

#rest_framework 
from rest_framework import serializers
from rest_framework.serializers import StringRelatedField
#serializers
from hyk.users.serializers import UserSerializer
#models
from hyk.users.models import Profile







class ProfileSerializer (serializers.ModelSerializer):
    user = UserSerializer(read_only =True , many = False)
    class Meta:
        model = Profile
        fields = ('__all__')






class ProfileSerializerListExtra(serializers.ModelSerializer):
    user = UserSerializer(read_only =True , many = False)
    
    class Meta:
        model = Profile
        fields = ('id' , 'user' ,'atlhetic_discipline')



class ProfileSerializerCreate (serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'weight',
            'height',
            'imc',
            'atlhetic_discipline'
        )



class ProfileSerializerALL (serializers.ModelSerializer):
    user = UserSerializer(read_only =True , many = False)
    rutines = serializers.SlugRelatedField(read_only=True,many=True, slug_field='name' )
    class Meta:
        model = Profile
        fields = ('__all__')




