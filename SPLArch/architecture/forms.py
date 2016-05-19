from SPLArch.architecture.models import *
from django.forms import IntegerField, TextInput, CharField
import datetime
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple


class ApiForm(forms.ModelForm):
    class Meta:
        model = API

    def clean(self):
        for field in self.cleaned_data:
            if isinstance(self.cleaned_data[field], basestring):
                self.cleaned_data[field] = self.cleaned_data[field].strip()
        return self.cleaned_data


class ReferencesForm(forms.ModelForm):
    #pages = CharField(widget=TextInput(attrs={'type':'number', 'required': ''}))
    #number = CharField(widget=TextInput(attrs={'type':'number'}))
    #volume = CharField(widget=TextInput(attrs={'type':'number'}))
    year = CharField(widget=TextInput(attrs={'type':'number', 'pattern':'^\d{4}$', 'max': datetime.datetime.now().year}))

    class Meta:
        model = References

    def clean(self):
        for field in self.cleaned_data:
            if isinstance(self.cleaned_data[field], basestring):
                self.cleaned_data[field] = self.cleaned_data[field].strip()
        return self.cleaned_data


class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology

    def clean(self):
        for field in self.cleaned_data:
            if isinstance(self.cleaned_data[field], basestring):
                self.cleaned_data[field] = self.cleaned_data[field].strip()
        return self.cleaned_data


class UseCaseForm(forms.ModelForm):
    class Meta:
        model = UseCase

    def __init__(self, *args, **kwargs):
        super(UseCaseForm, self).__init__(*args, **kwargs)
        wtf = Requirement.objects.filter(
            requirement_type=RequirementType.objects.filter(name='Functional Requirements'))

        w = self.fields['f_requirements'].widget
        choices = []
        for choice in wtf:
            choices.append((choice.id, choice.name))
        w.choices = choices

    def clean(self):
        for field in self.cleaned_data:
            if isinstance(self.cleaned_data[field], basestring):
                self.cleaned_data[field] = self.cleaned_data[field].strip()
        return self.cleaned_data


class ArchitectureForm(forms.ModelForm):
    class Meta:
        model = Architecture

    def clean(self):
        for field in self.cleaned_data:
            if isinstance(self.cleaned_data[field], basestring):
                self.cleaned_data[field] = self.cleaned_data[field].strip()
        return self.cleaned_data


class ScenariosForm(forms.ModelForm):
    class Meta:
        model = Scenarios

    def clean(self):
        for field in self.cleaned_data:
            if isinstance(self.cleaned_data[field], basestring):
                self.cleaned_data[field] = self.cleaned_data[field].strip()
        return self.cleaned_data


class DSSAForm(forms.ModelForm):

    class Meta:
        model = DDSA

    requirements = forms.ModelMultipleChoiceField(
        queryset=Requirement.objects.all().order_by('-priority'),
        widget=FilteredSelectMultiple(
            'requirements',
            False
        ),
        label='Architectural Drives (Requirements)'
    )

    def __init__(self, *args, **kwargs):
        super(DSSAForm, self).__init__(*args, **kwargs)
        self.fields['requirements'].label_from_instance = lambda obj: "%s" % obj.name + ' (' + obj.priority.name + ')'

    def clean(self):
        for field in self.cleaned_data:
            if isinstance(self.cleaned_data[field], basestring):
                self.cleaned_data[field] = self.cleaned_data[field].strip()
        return self.cleaned_data


class QualityScenariosForm(forms.ModelForm):
    class Meta:
        model = QualityScenarios

    def __init__(self, *args, **kwargs):
        super(QualityScenariosForm, self).__init__(*args, **kwargs)
        wtf = Requirement.objects.filter(
            requirement_type=RequirementType.objects.filter(name='Non-functional requirement'))

        w = self.fields['nf_requirement'].widget
        choices = []
        for choice in wtf:
            choices.append((choice.id, choice.name))
        w.choices = choices

    def clean(self):
        for field in self.cleaned_data:
            if isinstance(self.cleaned_data[field], basestring):
                self.cleaned_data[field] = self.cleaned_data[field].strip()
        return self.cleaned_data