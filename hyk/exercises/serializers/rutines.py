

#restframework
from rest_framework import serializers

#serializers
from hyk.users.serializers import ProfileSerializerListExtra
from hyk.exercises.serializers import ExercisesSerializer

#models
from hyk.exercises.models import Rutine , Exercises
from hyk.information.models import Info_Sessions




class RutineSerializerList(serializers.ModelSerializer):
    created_of = ProfileSerializerListExtra(read_only=True)
    exercises = ExercisesSerializer(read_only=True , many =True)
    class Meta:
        model = Rutine
        fields = ('id','created_of' , 'name' ,'description', 'exercises' , 'created' )



class RutineSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Rutine
        fields = ('description' , 'name')


    def create(self , validated_data):
        profile = self.context['profile']

        rutine = Rutine.objects.create(
            created_of = profile , 
            name=validated_data['name'],
            description= validated_data['description']
            )
        rutine.save()
        return rutine


class RutineSerializerAddExercise(serializers.Serializer):
    exercise = serializers.IntegerField(min_value=0)

    def validate_exercise (self , data):
        id_exercise = data 

        try :
            exercise = Exercises.objects.filter(id=id_exercise)
            
            if len(exercise) == 0 :
                raise serializers.ValidationError('exercise not exist :c ')
        except :
             serializers.ValidationError('exercise not exist :c ')
       

        return data


