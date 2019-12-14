#django
from django.db import models 

#utils
from hyk.utils.models.abstract_hyb import HybModel

class Info ( HybModel):
    cals_burn = models.IntegerField()
    kmR = models.IntegerField()
    #Resistencia
    #Fuerza
    #musculatura
    class Meta:
        abstract = True