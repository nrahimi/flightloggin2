from django.forms.models import modelformset_factory
from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from django.contrib.auth.models import User

from django import forms
from django.db.models import get_model

class NonFlightForm(ModelForm):
    class Meta:
        model = get_model('records', 'NonFlight')
        exclude = ('user' )
        
##############################
##############################
        
class CustomForm(ModelForm):
    coordinates = forms.CharField(widget=forms.TextInput(), required=False, help_text="In decimal format (e.g.: 34.322631,-84.481517)")
    
    class Meta:
        model = get_model('airport', 'Location')
        exclude = ('user' )
