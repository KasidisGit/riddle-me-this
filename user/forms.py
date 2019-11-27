from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = NameUser
        fields = [
            'name',
        ]
    
    class Meta:
        model = User
        fields = [
            'all_score',
        ]