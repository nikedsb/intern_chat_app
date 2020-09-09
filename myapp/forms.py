from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User,Message


class UserForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','img']


class LoginForm (AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

class MessageForm(forms.Form):
    content = forms.CharField(label='')

class FindForm(forms.Form):
    find = forms.CharField(label='search', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))