from django import forms
from django.contrib.auth.models import User
from .models import Profile, HelpMe, IcanHelp
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm


class AuthUserForm(AuthenticationForm, forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class CreateUserForm(ModelForm):

    class Meta:
        model = Profile
        fields = ('fio', 'avatar',
                  'email', 'number',
                  'speciality', 'well',
                  'add_information')


class HelpMeForm(ModelForm):

    class Meta:
        model = HelpMe
        fields = ('item', 'add_information')


class IcanHelpForm(ModelForm):

    class Meta:
        model = IcanHelp
        fields = ('items', 'skills')

