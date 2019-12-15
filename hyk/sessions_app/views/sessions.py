
from django.db.models import Q
#rest framework
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

#models 
from hyk.users.models import Profile
from hyk.exercises.models import Sessions


#serializers 
from hyk.sessions_app.serializers import SessionsSerializer , SessionsSerializerCreate






class SessionsViewset(
    mixins.ListModelMixin , 
    mixins.RetrieveModelMixin , 
    mixins.CreateModelMixin , 
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):



    def dispatch(self , request , *args , **kwargs):
       
        self.profile = get_object_or_404( Profile,user = int(kwargs['profile']))
      

        return super(SessionsViewset,self).dispatch(request , *args,**kwargs)

    permission_classes = [IsAuthenticated,]
    def get_queryset(self ):
        if self.profile.user != self.request.user :
            raise serializers.ValidationError('unauthorized')
        queryset = []
        if self.action in ['list' , 'retrieve' , 'create']:
            queryset = Sessions.objects.filter(session_profile=self.profile)
        else :
            queryset=Sessions.objects.filter(session_profile=self.profile)
        
        return queryset


    def get_serializer_class(self):
        
        if self.action in ['list' , 'retrieve' ]:
            serializer = SessionsSerializer
        else :
            serializer = SessionsSerializerCreate
        
        return serializer
    


    