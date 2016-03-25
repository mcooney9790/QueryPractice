__author__ = 'mcooney9790'

#from .models import Cities
from django import forms
#from __future__ import unicode_literals

class questionForm(forms.Form):
    this_question = forms.CharField(label='Question No', max_length=100)

class PostForm(forms.ModelForm):
    class Meta:
        # exclude = ['author', 'updated', 'created', ]
        fields = ['text']
        widgets = {
            'text': forms.TextInput(
                attrs={'id': 'post-text', 'required': True, 'placeholder': 'Say something...'}
            ),
        }


