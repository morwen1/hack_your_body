#django
from django.db import models 

#utils
from hyk.utils.models.abstract_hyb import HybModel
from .Info_abstract import Info


class Info_rutine (Info) :
    reps = models.IntegerField()
