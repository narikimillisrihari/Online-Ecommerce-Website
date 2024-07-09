from django.forms import ModelForm
from user.models import Profile
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]


class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields=["consumer","seller"]