'''
Created on Jun 4, 2012

@author: tadeo
'''
from django.forms.forms import Form
from django.forms.fields import CharField, EmailField
from django import forms
from django.utils.translation import ugettext_lazy as _

class SubscribeForm(Form):
    user_name = CharField(max_length=200, min_length=3, label=_('User name'))
    email = EmailField()
    message = CharField(widget=forms.Textarea, required=False)
