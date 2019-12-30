#django
from django.db import models 
#utils
from hyk.utils.models.abstract_hyb import HybModel
#models
from hyk.users.models import Profile
from hyk.information.models import Info_Sessions
from hyk.exercises.models import Rutine



    

 
class Sessions(HybModel):
    """
    Tabla intermedia de perfil a rutinas para poder obtener una session
    de entrenamiento , esto me ayudara para poder observar cuando un atleta hace
    una rutina , pero es indiferente de cuando la cree
    """
    session_profile  = models.ForeignKey(
        related_name='session_profile',
        to=Profile ,on_delete=None
        )
    session_rutines = models.ForeignKey(
        related_name ='session_rutines',
        to=Rutine , on_delete=None
    )
    
    info_session =models.ForeignKey(to=Info_Sessions , null =True, on_delete=models.CASCADE)
    duration = models.TimeField()
    def __str__(self):
        return f"{self.session_profile} , {self.session_rutines}"