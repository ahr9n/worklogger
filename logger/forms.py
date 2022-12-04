import datetime
from .models import Log, Project
from django import forms
from django.core.validators import MinValueValidator

class LogForm(forms.ModelForm):
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

    class Meta:
        model = Log
        fields = ["duration", "day", "project", "description"]


class ViewForm(forms.ModelForm):
    day = forms.DateField(
        required=True,
        widget=forms.widgets.DateInput(attrs={"type": "date"}),
        initial=datetime.date.today,
    )
    class Meta:
        model = Log
        fields = ["day"]
