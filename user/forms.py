from django import forms
from .models import NameUser


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(size='20', placeholder='Your name here')
        self.fields['name'].label = ""

    class Meta:
        model = NameUser
        fields = ['name']

    