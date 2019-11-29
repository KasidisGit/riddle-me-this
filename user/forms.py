from django import forms
from .models import NameUser

class UserForm(forms.ModelForm):
    class Meta:
        model = NameUser
        fields = [
            'name',
        ]
