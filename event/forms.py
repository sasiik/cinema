# forms.py
from django import forms

class ParticipateForm(forms.Form):
    event_id = forms.IntegerField(widget=forms.HiddenInput())
