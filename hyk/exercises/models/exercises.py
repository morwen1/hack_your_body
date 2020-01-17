#Django
from django.db import models
#models
from hyk.utils.models.abstract_hyb import HybModel
from hyk.users.models import Profile


"""
Los ejercicios son creados y nombrados por el usuario
falta saber como obtener el tipo de ejercicio para adecuar la informacion 
del mismo 
"""

class ExercisesType(HybModel):
    exercise_type = models.CharField(max_length=255)
    information_type = models.CharField(max_length=255)


class InstructionsExercises( HybModel):
    text = models.CharField(max_length=255)
    recomendations = models.CharField(max_length=255)
    warnings = models.CharField(max_length=255)


class Exercises ( HybModel):
    created_of = models.ForeignKey(to= Profile , on_delete = None)
    name= models.CharField(max_length=255 , unique=True)
    description = models.CharField(max_length=255)
    exercise_type  = models.ManyToManyField(to=ExercisesType)
    instructions = models.OneToOneField(to=InstructionsExercises , on_delete=None)