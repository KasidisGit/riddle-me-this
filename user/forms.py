from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name'
        ]

# class CustomUserForm(forms.Form):
#     name = forms.CharField(max_length=254, null=True, blank=True, default=True)