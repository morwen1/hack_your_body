#django
from django.db import models 

#utils
from hyk.utils.models.abstract_hyb import HybModel

class Info ( HybModel):
    """
    cals =calorias que se gastaron al hacer el ejercicio o rutina
    ritcard = ritmo cardiaco promedio mientras se hacia la actividad fisica
    pasos= pasos dados mientras se hacia la actividad fisica
    kmr = kilometros recorridos
    ptRute = porentaje de la ruta culminado
    """
    ritcard = models.IntegerField(null=True)
    steps = models.IntegerField(null=True)
    kmr=models.IntegerField(null=True)
    ptRute=models.IntegerField(null=True)
    cals_burn = models.IntegerField(null=True)
    kmR = models.IntegerField(null=True)
    dur_time = models.TimeField(null=True)
    
    class Meta:
        abstract = True