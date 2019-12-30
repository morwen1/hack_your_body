from rest_framework import serializers
from hyk.exercises.models import Info_Sessions



class Info_sessions_Serializer (serializers.ModelSerializer):
    class Meta:
        model= Info_Sessions
        fields = '__all__'
        read_only_fields = ('id','created','deleted')