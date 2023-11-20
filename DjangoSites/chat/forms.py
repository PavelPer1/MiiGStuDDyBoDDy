from django.forms import ModelForm
from django import forms

from chat.models import Message


class MessageForm(ModelForm):
    message = forms.CharField(max_length=300)

    class Meta:
        model = Message
        fields = ['message']
