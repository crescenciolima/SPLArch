from django import forms
from .models import *

class QualityForm(forms.ModelForm):
    class Meta:
        model = Quality

    def clean(self):
        for field in self.cleaned_data:
            if isinstance(self.cleaned_data[field], basestring):
                self.cleaned_data[field] = self.cleaned_data[field].strip()
        return self.cleaned_data