from django.db import models

class Variable(models.Model):

    name = models.CharField(max_length=100, unique=True) 
    TYPE_CHOICES = (
        ('I', 'Integer'),
        ('F', 'Float')
    )
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='F')
    default = models.FloatField(default=-1111.)
    min = models.FloatField(default=0.)
    max = models.FloatField(default=1.)
    one_prong = models.BooleanField()
    three_prong = models.BooleanField()
    fancy = models.CharField(max_length=200, blank=True)
    alias = models.CharField(max_length=100, blank=True, unique=True)
    units = models.CharField(max_length=3, default='', blank=True)
    displayunits = models.CharField(max_length=3, default='', blank=True)

    def __unicode__(self):

        return self.name
