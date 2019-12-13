from django.db import models



class HybModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.DateTimeField(null=True)
    class Meta:
        abstract = True