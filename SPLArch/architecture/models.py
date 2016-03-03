from SPLArch.scoping.models import *
from SPLArch.requirement.models import *
from SPLArch.architecture.models import *
from django.db import models
from django.contrib.auth.models import *
from django.core import urlresolvers
from django.contrib.contenttypes.models import ContentType
from SPLArch.architecture.util import render_to_latex


PRIORITY = (
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
)


class References(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    publisher = models.CharField(max_length=100, blank=True)
    pages = models.CharField(max_length=7, blank=True)
    number = models.IntegerField(max_length=4, blank=True)
    year = models.IntegerField(max_length=4)
    volume = models.IntegerField(max_length=4, blank=True)

    def __unicode__(self):
        return self.title

    @staticmethod
    def getReport(product=None):
        if (product):
            mycontext = {'references': References.objects.all,
                         'product_name': product.name,
                         'autoescape': False}
        else:
            mycontext = {'references': References.objects.all,
                         'product_name': "All products",
                         'autoescape': False}

        return render_to_latex("admin/fur/references/report_references.tex", mycontext)

    class Meta:
        verbose_name = "References"
        verbose_name_plural = "References"


class DDSA(models.Model):
    name = models.CharField(max_length=100)
    introduction = models.TextField(blank=True)
    references = models.ManyToManyField('References')
    technology = models.ManyToManyField('Technology')
    quality_attribute_priority = models.ManyToManyField('QualityScenarios', through='QualityAttributePriority')
    requirements = models.ManyToManyField(Requirement,)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "DSSA"
        verbose_name_plural = "DSSAs"

    @staticmethod
    def getReport(product=None):
        if (product):
            mycontext = {'dssas': DDSA.objects.all,
                         'product_name': product.name,
                         'autoescape': False}
        else:
            mycontext = {'dssas': DDSA.objects.all,
                         'product_name': "All products",
                         'autoescape': False}

        return render_to_latex("admin/fur/dssa/report_dssa.tex", mycontext)


class QualityAttributePriority(models.Model):
    add_scenarios = models.ForeignKey('QualityScenarios', on_delete=models.CASCADE, verbose_name='Quality Scenario')
    dssa = models.ForeignKey('DDSA', on_delete=models.CASCADE)
    priority = models.CharField(max_length=64, choices=PRIORITY)

    def __unicode__(self):
        return self.add_scenarios.name + " " + self.priority

class QualityScenarioDocument(models.Model):
    introduction = models.TextField(blank=True)
    references = models.ManyToManyField('References')
    quality_scenarios = models.ManyToManyField('QualityScenarios')

    def __unicode__(self):
        return self.introduction

    class Meta:
        verbose_name = "Quality Scenario Document"
        verbose_name_plural = "Quality Scenario Documents"

    @staticmethod
    def getReport(product=None):
        if (product):
            mycontext = {'qualityscenariodocuments': QualityScenarioDocument.objects.all,
                         'product_name': product.name,
                         'autoescape': False}
        else:
            mycontext = {'qualityscenariodocuments': QualityScenarioDocument.objects.all,
                         'product_name': "All products",
                         'autoescape': False}

        return render_to_latex("admin/fur/qualityscenariodocument/report_qualityscenariodocument.tex", mycontext)


class Scenarios(models.Model):
    name = models.CharField(max_length=100)
    stimulus = models.TextField(blank=True)
    response = models.TextField(blank=True)
    strategy = models.TextField(blank=True)
    feature = models.ManyToManyField(Feature)
    nf_requirement = models.ManyToManyField(Requirement)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Scenario Detail"


class QualityScenarios(models.Model):
    name = models.CharField(max_length=100)
    nf_requirement = models.ManyToManyField(Requirement)
    scenario = models.OneToOneField(Scenarios)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Quality Scenario"
        verbose_name_plural = "Quality Scenarios"


class Technology(models.Model):
    api = models.ManyToManyField('API', verbose_name="API")
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.description

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"

    @staticmethod
    def getReport(product=None):
        if (product):
            mycontext = {'technologies': Technology.objects.all,
                         'product_name': product.name,
                         'autoescape': False}
        else:
            mycontext = {'technologies': Technology.objects.all,
                         'product_name': "All products",
                         'autoescape': False}

        return render_to_latex("admin/fur/technologies/report_technologies.tex", mycontext)


class API(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    specification = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "API"
        verbose_name_plural = "APIs"

    @staticmethod
    def getReport(product=None):
        if (product):
            mycontext = {'api': API.objects.all,
                         'product_name': product.name,
                         'autoescape': False}
        else:
            mycontext = {'api': API.objects.all,
                         'product_name': "All products",
                         'autoescape': False}

        return render_to_latex("admin/fur/api/report_api.tex", mycontext)



class Architecture(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    references = models.ManyToManyField('References', blank=True, symmetrical=False, related_name='mainsteps_funcspec')

