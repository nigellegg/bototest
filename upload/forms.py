
from django import forms
from django.core.exceptions import ValidationError


class upcsvForm(forms.Form):
    csvx = forms.FileField(
        label='File name',
        required=False)
    csvname = forms.CharField(
        label='Note')
