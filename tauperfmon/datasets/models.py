from django.db import models

class Dataset(models.Model):

    name = models.CharField(max_length=100, unique=True) 
    
    TYPE_CHOICES = (
        ('I', 'Integer'),
        ('F', 'Float')
    )
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='F')

    def __unicode__(self):

        return self.name
