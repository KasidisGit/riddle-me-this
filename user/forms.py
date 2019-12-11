
from django import forms
from .models import User


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = ""
        self.fields['name'].widget =  forms.HiddenInput()

    class Meta:
        model = User
        fields = ['name']

    