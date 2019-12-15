#django
from django.db import models 
#utils
from hyk.utils.models.abstract_hyb import  HybModel
#models 
from hyk.users.models import Profile

from hyk.information.models import Info_rutine ,Info_Month


class Rutine (HybModel):
    """
    Este modelo refleja las rutinas creadas por un perfil 
    una rutina tiene varios ejercicios y una informacion por mes y por rutina
    """
    created_of = models.ForeignKey( related_name='created_of',to=Profile , on_delete = None)
    name = models.CharField(max_length=255)
    exercises = models.ManyToManyField(to='exercises.Exercises')
    description = models.TextField()
    info_rutine = models.ForeignKey(to=Info_rutine , null=True,on_delete=models.CASCADE)
    info_month = models.ManyToManyField(to=Info_Month )
    sessions = models.ManyToManyField(
        to=Profile ,
        through='exercises.Sessions', 
        through_fields=('session_rutines' ,'session_profile' ),
        help_text = "this field is for register data of the day or session training with the self rutine"
    )

    def __str__(self):
        return f" created of: {self.created_of}, name: {self.name}"