from dataclasses import field
import imp
from socket import fromshare
from django import forms
from . models import Notes
from django.core.exceptions import ValidationError


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets= {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'text' : forms.Textarea(attrs={'class':'form-control'}),
        }
        labels = {
            'text': 'Write your Note',
            'title': 'Note Title'

        }

    def clean_title(self):
        title =self.cleaned_data['title']
        for character in title:
            if character.isdigit():
                 raise ValidationError('digit number not allowed in title')   
        return title
        