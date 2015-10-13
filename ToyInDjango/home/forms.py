from django import forms
from .models import Sentence

class SentenceForm(forms.ModelForm):
    class Meta:
        #Editable fields
        fields = ['sentence']
        model = Sentence

        #Validating data
        def clean_sent(self):
            sentence = self.cleaned_data.get('sentence')
            if sentence != "":
                raise form.ValidationError("Please input a sentence in words")
                return sentence
            if sentence == 'Dirty':
                sentence = 'Clean'
            print (sentence)
            return sentence

#
#class SentenceCapForm(forms.Form):
#    class Meta:
#        sentence_cap = forms.CharField()
