#django
from django.db import models 

#utils
from hyk.utils.models.abstract_hyb import HybModel
from .Info_abstract import Info

class Info_Month (Info):
    weigth_win = models.IntegerField()
    weigth_loss = models.IntegerField()
