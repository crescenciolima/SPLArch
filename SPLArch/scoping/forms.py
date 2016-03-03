from SPLArch.requirement.models import *
from django.forms import *
from mptttreewidget.widget import MpttTreeWidget
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple



class ProductMapForm(ModelForm):
    features = ModelMultipleChoiceField(required=False, queryset=Feature.objects.all(), widget=MpttTreeWidget)

    class Meta:
        model = Feature

    def clean(self):
        for field in self.cleaned_data:
            if isinstance(self.cleaned_data[field], basestring):
                self.cleaned_data[field] = self.cleaned_data[field].strip()
        return self.cleaned_data


class RequirementForm(forms.ModelForm):
    class Meta:
        model = Requirement

    def clean(self):
        for field in self.cleaned_data:
            if isinstance(self.cleaned_data[field], basestring):
                self.cleaned_data[field] = self.cleaned_data[field].strip()
        return self.cleaned_data


class GlossaryForm(forms.ModelForm):
    class Meta:
        model = Glossary

    def clean(self):
        for field in self.cleaned_data:
            if isinstance(self.cleaned_data[field], basestring):
                self.cleaned_data[field] = self.cleaned_data[field].strip()
        return self.cleaned_data


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project

    def clean(self):
        for field in self.cleaned_data:
            if isinstance(self.cleaned_data[field], basestring):
                self.cleaned_data[field] = self.cleaned_data[field].strip()
        return self.cleaned_data


class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature

    def clean(self):
        for field in self.cleaned_data:
            if isinstance(self.cleaned_data[field], basestring):
                self.cleaned_data[field] = self.cleaned_data[field].strip()
        return self.cleaned_data




