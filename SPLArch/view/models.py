from django.db import models
from SPLArch.component.models import *


# Create your models here.

class ViewPoint(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    stakeholder = models.CharField(max_length=100)
    concern = models.CharField(max_length=100)
    componentOne = models.OneToOneField(Components, related_name='ComponentOne')
    componentTwo = models.OneToOneField(Components, related_name='ComponentTwo')
    relationship = models.CharField(max_length=100)
    property = models.CharField(max_length=100)
    restriction = models.CharField(max_length=100)
    viewPointRelated = models.ManyToManyField("self", blank=True)

    class Meta:
        verbose_name = 'View Point Item'
        verbose_name_plural = 'View Point'

    def __unicode__(self):
        return self.name


class Quality(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class VariabilityGuidelines(models.Model):
    stimulus = models.CharField(max_length=100)
    reaction = models.CharField(max_length=100)
    strategy = models.CharField(max_length=100)
    feature = models.CharField(max_length=100)
    qualityAtributes = models.ManyToManyField('Quality')

    class Meta:
        verbose_name = 'Variability Item'
        verbose_name_plural = 'Variability Guideline'

    def __unicode__(self):
        return self.stimulus


class View(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    stakeholder = models.CharField(max_length=100)
    concern = models.CharField(max_length=100)
    diagram = models.CharField(max_length=100)
    viewPointRelated = models.ManyToManyField(ViewPoint)
    variabilityGuidelines = models.ManyToManyField(VariabilityGuidelines, related_name='Variability View')

    class Meta:
        verbose_name = 'View Item'
        verbose_name_plural = 'View'

    def __unicode__(self):
        return self.name


class StructuralView(models.Model):
    presentation = models.CharField(max_length=200)
    architectureStyle = models.CharField(max_length=200)
    modelDiagram = models.CharField(max_length=100)
    model = models.ManyToManyField(Module)
    viewPointRelated = models.ManyToManyField(ViewPoint)
    variabilityGuidelines = models.ManyToManyField(VariabilityGuidelines, related_name='Variability Structural')

    class Meta:
        verbose_name = 'Structural Vision Item'
        verbose_name_plural = 'Structural Vision'

    def __unicode__(self):
        return self.presentation


class BehaviorView(models.Model):
    diagram = models.CharField(max_length=100)
    featuresRelated = models.ManyToManyField(Feature, related_name='Feature Behavior')
    sequenceDiagram = models.CharField(max_length=100)
    viewPointRelated = models.ManyToManyField(ViewPoint)
    variabilityGuidelines = models.ManyToManyField(VariabilityGuidelines, related_name='Variability Behavior')

    class Meta:
        verbose_name = 'Behavior Vision Item'
        verbose_name_plural = 'Behavior Vision'
