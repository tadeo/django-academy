'''
Created on Jun 4, 2012

@author: tadeo
'''
from django.forms.forms import Form
from django.forms.models import ModelForm
from django.forms.fields import CharField, EmailField, IntegerField
from django import forms
from django.utils.translation import ugettext_lazy as _
from apps.main.models import Subscriber

class SubscribeForm(Form):
    user_name = CharField(max_length=200, min_length=3, label=_('User name'))
    email = EmailField()
    message = CharField(widget=forms.Textarea, required=False)
    age = IntegerField()


class SubscriberForm(ModelForm):
    class Meta:
        model = Subscriber

class SimplifiedSubscriberForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = ['name','email']

class ExtendedSubscriberForm(ModelForm):
    class Meta:
        model = Subscriber

