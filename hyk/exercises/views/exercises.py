
# django

from django.db.models import Prefetch
# rest_framework

from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
# serializers
from hyk.exercises.serializers import (
    ExercisesSerializer ,
    ExercisesSerializerCreate ,
    ProfileSerializerListExtra ,
    ExercisesSerializerUpdate ,
    InstructionsSerializers,)
# models
from hyk.exercises.models import Exercises
from hyk.users.models import Profile
#mixins

from hyk.exercises.views.mixins_views import context_views

class ExercisesViewset(
    context_views,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
    
):

    """
    /exercises/exercises/
        create , list
    
    /exercises/exercises/{id}/
        update  exercise , retrieve

    /exercises/exercises/{id}/update_instructions/
        i can update instructions of that exercise
    
    fields created and deleted no editables
    """



    def get_serializer_class(self):

        if self.action in ['create' ]:
            serializer = ExercisesSerializerCreate
        if self.action in ['update' , 'partial_update']:
            serializer = ExercisesSerializerUpdate
        if self.action in ['list' ,'retrieve'] :
            serializer = ExercisesSerializer
        if self.action == 'update_instructions':
            serializer = InstructionsSerializers
        return serializer


    def get_queryset(self):
        queryset = []
        if self.action in ['list' , 'retrieve']:
            queryset = Exercises.objects.all()
        if self.action in ['update', 'partial_update','create' , 'update_instructions']:
            user = self.request.user
            profile = Profile.objects.get(user=user)
            queryset = Exercises.objects.filter(created_of=profile)
        if queryset != []:
            queryset.prefetch_related(Prefetch('instructions'))
        return queryset
 
    def get_permissions(self):
        permissions = []
        if self.action == 'list':
            permissions = [AllowAny]
        if self.action in ['create','update', 'partial_update' ,'update_instructions']:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]


    @action(methods = ['PUT' , 'PATCH'] , detail= True)
    def update_instructions( self , request, pk=None ):
        """
        action to update instructions filter of pk exercise
        exercise -> instructions 
        
        """
        queryset = self.get_queryset()
        instance = queryset.get(id=pk).instructions
        serializer = self.get_serializer(instance , data=request.data , partial = True)
        serializer.is_valid(raise_exception =True)
        serializer.save()
        return Response(data = serializer.data , status = 200)
