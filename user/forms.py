from django import forms
from .models import NameUser


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = ""
        self.fields['name'].widget =  forms.HiddenInput()

    class Meta:
        model = NameUser
        fields = ['name']

    