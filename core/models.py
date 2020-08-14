from django.db import models

""" Author : PresentJay """

class TimeStampedModel(models.Model):
    
    """ Time Stamped Model """
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True