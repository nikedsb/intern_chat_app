from django.contrib.auth import forms as auth_forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser, ChatContent
from django import forms


class SignUpForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'img')


class LoginForm(auth_forms.AuthenticationForm):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label


class ChatForm(forms.ModelForm):

    class Meta:
        model = ChatContent
        fields = ('chat_content',)
