#django
from django.db import models 

#utils
from .Info_abstract import Info


class Info_Sessions (Info) :
    time = models.TimeField(null=True)
    intensity = models.IntegerField(null=True)
