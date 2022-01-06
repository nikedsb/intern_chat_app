from os import truncate
from django import forms
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField, TextField
from django.forms import fields, widgets
from django.forms.forms import Form
from django.contrib.auth.forms import AuthenticationForm

from myapp.models import CustomUser
from myapp.models import Message

# 最適化に使うやつ
from allauth.account.forms import SignupForm
from django.core.exceptions import ValidationError

def clean_image(img):
    '''サインアップ時の画像サイズが大きいとエラーを出す関数'''
    if img:
        if img.size > 2*1024*1024:
            # comout print('file too large')
            raise ValidationError('ファイルサイズは2MB以下にしてください')
        return img
    else:
        raise ValidationError('画像を読み込めませんでした')

class CustomSignUpForm(SignupForm):
    image = fields.ImageField(
        required=False,
        label='image',
        validators=[clean_image],
    )

    def save(self, request):
        user = super(CustomSignUpForm, self).save(request)
        return user

    class Meta:
        model = CustomUser

class MessageForm(forms.Form):
    content = forms.CharField(
        label="message", 
        required=True,
        max_length=1000,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
            }
        )
    )

class UserUpdateForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        required=True,
        label="Username",
    )
    email = forms.EmailField(
        max_length=100,
        required=True,
        label="Email",
    )
    image = forms.ImageField(
        required=True,
        label="Image",
    )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'image')