from django import forms
from .models import DataSet


class RecordForm(forms.ModelForm):
    class Meta:
        model = DataSet
        fields = ('author', 'content')
