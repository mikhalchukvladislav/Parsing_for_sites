from django.forms import ModelForm
from .models import *
from django import forms


class CreateForm(ModelForm):

    class Meta:
        model = Url
        fields = ['link']