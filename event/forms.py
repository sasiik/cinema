# forms.py
from django import forms

# Form for "film" and "event" type events

class ParticipateForm(forms.Form):
    event_id = forms.IntegerField(widget=forms.HiddenInput())
    selected_seat = forms.CharField(widget=forms.HiddenInput(), required=False)