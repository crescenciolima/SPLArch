from django.db import models

from django.contrib.auth.models import *
from django.core import urlresolvers
from django.contrib.contenttypes.models import ContentType
from SPLArch.architecture.util import render_to_latex
from SPLArch.architecture.models import *
from SPLArch.requirement.models import *
from SPLArch.scoping.models import *


STATUS_REQUIREMENT_CHOICES = (
    ('proposed', 'Proposed'),
    ('approved', 'Approved'),
    ('implemented', 'Implemented'),
    ('verified', 'Verified'),
    ('deferred', 'Deferred'),
    ('deleted', 'Deleted'),
    ('rejected', 'Rejected'),
)

PRIORITY = (
    ('no priority', 'No Priority'),
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
    ('very high', 'Very High'),
    ('Urgent', 'Urgent'),
)


class PriorityRequirement(models.Model):
    name = models.CharField(max_length=200)
    level = models.IntegerField(max_length=10)

    def __unicode__(self):
        return self.name




class RequirementType(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name


class Requirement(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    observations = models.TextField(blank=True)
    status_requirement_choices = models.CharField(max_length=200, choices=STATUS_REQUIREMENT_CHOICES, verbose_name='Status')
    requirement_type = models.ForeignKey('RequirementType')
    feature = models.ManyToManyField(Feature)
    priority = models.ForeignKey('PriorityRequirement')

    def __unicode__(self):
        return self.name


    @staticmethod
    def getReport(product=None):
        if(product):
            mycontext = {'requirements': Requirement.objects.all,
                         'product_name': product.name,
                         'autoescape': False
            }
        else:
            mycontext = {'requirements': Requirement.objects.all,
                         'product_name': "All products",
                         'autoescape': False
            }

        return render_to_latex("admin/fur/requirement/report_requirement.tex",mycontext)


class UseCase(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    precondition = models.TextField(max_length=200, blank=True,verbose_name="Pre-condition")
    feature = models.ManyToManyField(Feature, blank=True, symmetrical=False)
    mainSteps = models.ManyToManyField('MainSteps', blank=True, symmetrical=False, related_name='mainsteps_funcspec')
    owner = models.ManyToManyField(User, blank=False, symmetrical=False, related_name='owner_funcspec')
    alternativeSteps = models.ManyToManyField('AlternativeSteps', blank=True, symmetrical=False, related_name='alternativesteps_funcspec')
    f_requirements = models.ManyToManyField(Requirement)

    def __unicode__(self):
        return self.title
    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))

    @staticmethod
    def getReport(product=None):
        if(product):
            mycontext = {'usecases': UseCase.objects.filter(feature__in=product.features.all),
                         'product_name': product.name,
                   'autoescape': False}
        else:
            mycontext = {'usecases': UseCase.objects.all,
                         'product_name': "All products",
                    'autoescape': False}

        return render_to_latex("admin/fur/usecase/report_usecase.tex",mycontext)

class MainSteps(models.Model):
    use_case = models.ForeignKey(UseCase)
    user_action = models.TextField()
    system_response = models.TextField()
    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))
    def __unicode__(self):
        return "Main Step"

class AlternativeSteps(models.Model):
    use_case = models.ForeignKey(UseCase)
    user_action = models.TextField()
    system_response = models.TextField()
    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))
    def __unicode__(self):
        return "Alternative Step"

