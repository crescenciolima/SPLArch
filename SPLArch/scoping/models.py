from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core import urlresolvers
from SPLArch.architecture.util import render_to_latex

# Create your models here.

class BindingTime(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Feature binding time Item'
        verbose_name_plural = 'Feature binding times'

    def __unicode__(self):
        return self.name

VARIABILITY_CHOICES = (
    ('mandatory', 'Mandatory'),
    ('optional', 'Optional'),
    ('alternative', 'Alternative')
)
TYPE_CHOICES = (
    ('abstract', 'Abstract'),
    ('concrete', 'Concrete')
)

class Feature(MPTTModel):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    configuration = models.CharField(max_length=200)

    variability = models.CharField(max_length=20, choices=VARIABILITY_CHOICES)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    binding_time = models.ForeignKey('BindingTime')

    parent  = TreeForeignKey('self', blank=True, null=True, related_name='children')
    requires = models.ManyToManyField("self", blank=True)
    excludes = models.ManyToManyField("self", blank=True, symmetrical=False,
                                      related_name='excludes_features')
    glossary = models.ManyToManyField('Glossary', blank=True)

    def __unicode__(self):
        return "#" + str(self.id) + " "  + self.name


    class MPTTMeta:
        order_insertion_by = ['name']
    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))

    @staticmethod
    def getReport(product=None):
        if(product):
            mycontext = {'features': product.features.all,
                         'product_name': product.name,
                   'autoescape': False}
        else:
            mycontext = {'features': Feature.objects.all,
                         'product_name': "All products",
                    'autoescape': False}
        return render_to_latex("admin/fur/feature/report_features.tex",mycontext)


class Glossary(models.Model):
    term = models.CharField(max_length=200)
    definition = models.TextField(max_length=200)

    class Meta:
        verbose_name = 'Glossary Item'
        verbose_name_plural = 'Glossary'
    def __unicode__(self):
        return self.term
    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))
    @staticmethod
    def getReport(product=None):
        if(product):
            mycontext = {'glossary': Glossary.objects.filter(feature__in=product.features.all).distinct(),
                         'product_name': product.name,
                   'autoescape': False}
        else:
            mycontext = {'glossary': Glossary.objects.all,
                         'product_name': "All products",
                    'autoescape': False}

        return render_to_latex("admin/fur/glossary/report_glossary.tex",mycontext)


class Product(models.Model):
    name = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=True)
    features = models.ManyToManyField('Feature', blank=True, symmetrical=False)

    def __unicode__(self):
        return self.name

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    product = models.ManyToManyField(Product)

    def __unicode__(self):
        return self.name
    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))
