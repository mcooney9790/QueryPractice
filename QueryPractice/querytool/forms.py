__author__ = 'mcooney9790'

#from .models import Cities
from django import forms
#from __future__ import unicode_literals

class questionForm(forms.Form):
    this_question = forms.CharField(label='Question No', max_length=100)

