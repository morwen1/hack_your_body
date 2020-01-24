
# django

from django.db.models import Prefetch
# rest_framework
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly, AllowAny
# serializers
from hyk.exercises.serializers import RutineSerializerList , RutineSerializerCreate , RutineSerializerAddExercise
# models
from hyk.exercises.models import Rutine ,Exercises
from hyk.users.models import Profile
#mixins_views
from hyk.exercises.views.mixins_views import context_views



class RutineViewset(context_views,viewsets.ModelViewSet):

    
    
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = []
        if self.action in ['list' , 'retrieve']:
            queryset = Rutine.objects.all()

        if self.action in ['create' , 'update' , 'partial_update' ,'add_exercises' ,'remove_exercises']:
            profile = Profile.objects.get(user = self.request.user)
            queryset = Rutine.objects.filter(created_of = profile)
        
        if queryset != []:
            queryset = queryset.prefetch_related(
                Prefetch('exercises') , 
                Prefetch('created_of')
            )
        
        return queryset

    def get_serializer_class(self):
        serializer = RutineSerializerList
        if self.action in ['create' , 'update' , 'partial_update']:
            serializer = RutineSerializerCreate
        return serializer
    
    
    @action(methods = ['post'] , detail =True)
    def add_exercises(self, request , pk ):
        queryset = self.get_queryset()

        try:
            rutine = queryset.get(id=pk)
        except:
            raise serializers.ValidationError('you not have permited edit that rutine >:c')
        
        
        serializer = RutineSerializerAddExercise(data=request.data)
        serializer.is_valid(raise_exception=True)
        exercise = Exercises.objects.get(id =request.data['exercise'])
        rutine.exercises.add(exercise)
        return Response(data=RutineSerializerList(rutine).data , status = 201)

    
    @action(methods = ['post'] , detail =True)
    def remove_exercises(self, request , pk ):
        queryset = self.get_queryset()


        try:
            rutine = queryset.get(id=pk)
        except:
            raise serializers.ValidationError('you not have permited edit that rutine >:c')
        
        
        serializer = RutineSerializerAddExercise(data=request.data)
        serializer.is_valid(raise_exception=True)
        exercise = Exercises.objects.get(id =request.data['exercise'])
        rutine.exercises.remove(exercise)
        return Response(data=RutineSerializerList(rutine).data , status = 201)

        

        

