from SPLArch.architecture.models import *
from SPLArch.requirement.models import *
from django import forms


class RequirementForm(forms.ModelForm):
    class Meta:
        model = Requirement

    def clean(self):
        for field in self.cleaned_data:
            if isinstance(self.cleaned_data[field], basestring):
                self.cleaned_data[field] = self.cleaned_data[field].strip()
        return self.cleaned_data


class RequirementTypeForm(forms.ModelForm):
    class Meta:
        model = RequirementType

    def clean(self):
        for field in self.cleaned_data:
            if isinstance(self.cleaned_data[field], basestring):
                self.cleaned_data[field] = self.cleaned_data[field].strip()
        return self.cleaned_data
