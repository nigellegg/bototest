
from django import forms
from django.core.exceptions import ValidationError


class datafileForm(forms.Form):
    csvx = forms.FileField(
        label='File name',
        required=False)
    csvname = forms.CharField(
        label='Note')
