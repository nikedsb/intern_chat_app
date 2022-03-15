from django import forms
from .models import TalkModel,User
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,UserChangeForm,UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2','icon']


class LoginForm(AuthenticationForm):
    pass


class TalkForm(forms.ModelForm):
    class Meta:
        model = TalkModel
        fields = ['content']


class PasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    

class UpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username','email','icon']


class SearchForm(forms.Form):
    word = forms.CharField(max_length=100,label='友達検索')