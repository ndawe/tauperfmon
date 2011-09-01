from django.db import models

class Discriminant(models.Model):

    name = models.CharField(max_length=100, unique=True) 
    METHOD_CHOICES = (
        ('CUTS', 'Cut-based'),
        ('BDT', 'Boosted Decision Trees'),
        ('LLH', 'Likelihood')
    )
    type = models.CharField(max_length=4, choices=METHOD_CHOICES)
    min = models.FloatField(default=0.)
    max = models.FloatField(default=1.)

    def __unicode__(self):

        return "%s: %s" % (self.type, self.name)
