from django import forms
from .models import Sentence

class SentenceForm(forms.ModelForm):
    class Meta:
        #Editable fields
        fields = ['sentence']
        model = Sentence