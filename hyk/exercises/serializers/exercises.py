from rest_framework import serializers
#serializers
from hyk.users.serializers import ProfileSerializerListExtra

#models
from hyk.exercises.models import InstructionsExercises ,Exercises
from hyk.users.models import Profile



class InstructionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = InstructionsExercises
        exclude =('id','deleted' )



class ExercisesSerializer(serializers.ModelSerializer):
    instructions = InstructionsSerializers()
    created_of = ProfileSerializerListExtra(read_only=True)
    class Meta:
        model= Exercises
        fields = ('id', 'name' ,'description','instructions' ,'created_of' , 'created')
        



class ExercisesSerializerCreate(serializers.ModelSerializer):
    instructions = InstructionsSerializers()
    class Meta:
        model= Exercises
        fields = ('name' ,'description','instructions' )
        
    
    def create(self , validate_data):
        created_of = self.context['profile']
        instructions_data = validate_data.pop('instructions')
        instructions = InstructionsExercises.objects.create(**instructions_data)
        exercise = Exercises.objects.create(created_of=created_of,instructions =instructions,**validate_data)
        instructions.save()
        exercise.save()
        return exercise