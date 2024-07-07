from django import forms
from .models import *

class Contacfrom(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = '__all__'