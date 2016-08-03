from django.db import models
from SPLArch.scoping.models import *


# Create your models here.

class Components(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    features = models.ManyToManyField(Feature)
    modules = models.ManyToManyField('Module')
    variabilityGuidelines = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Component Item'
        verbose_name_plural = 'Component'

    def __unicode__(self):
        return self.name

class Module(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    features = models.ManyToManyField(Feature)

    class Meta:
        verbose_name = 'Module Item'
        verbose_name_plural = 'Module'

    def __unicode__(self):
        return self.name

class VariabilityGuidelines (models.Model):
    stimulus = models.CharField(max_length=100)
    reaction = models.CharField(max_length=100)
    strategy = models.CharField(max_length=100)
    feature = models.CharField(max_length=100)
    qualityAtributes = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Variability Item'
        verbose_name_plural = 'Variability'

    def __unicode__(self):
        return self.stimulus
