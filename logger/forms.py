import datetime
from .models import *
from django import forms
from django.core.validators import MinValueValidator


class LogForm(forms.Form):
    duration = forms.FloatField(
        required=True,
        widget=forms.TextInput(),
        initial=0,
        validators=[
            MinValueValidator(0),
        ],
    )
    day = forms.DateField(
        required=True,
        widget=forms.widgets.DateInput(attrs={"type": "date"}),
        initial=datetime.date.today,
    )
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    description = forms.CharField(required=True, widget=forms.TextInput())


class ViewForm(forms.Form):
    day = forms.DateField(
        required=True,
        widget=forms.widgets.DateInput(attrs={"type": "date"}),
        initial=datetime.date.today,
    )
