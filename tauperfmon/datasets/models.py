from django.db import models

class Dataset(models.Model):

    name = models.CharField(max_length=100, unique=True) 
    
    TYPE_CHOICES = (
        ('DATA', 'Data'),
        ('MC', 'Monte Carlo')
    )
    data_type = models.CharField(max_length=4, choices=TYPE_CHOICES, default='MC')
    
    CLASS_CHOICES = (
        ('SIGNAL', "Signal"),
        ('BACKGROUND', 'Background')
    )
    data_class = models.CharField(max_length=10, choices=CLASS_CHOICES, default='BACKGROUND')

    LABEL_CHOICES = (
        ('TAU', "Tau"),
        ('MUON', "Muon"),
        ('ELEC', "Electron"),
        ('JET', 'Jet background')
    )
    label = models.CharField(max_length=4, choices=LABEL_CHOICES, default='JET')

    weight = models.FloatField(default=1.)

    def __unicode__(self):

        return self.name
