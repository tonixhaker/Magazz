from django import forms
from .models import *


class OwnDateField(forms.DateInput):
    input_type = 'date'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['count']
        widgets = {
            'last_login': OwnDateField()
        }