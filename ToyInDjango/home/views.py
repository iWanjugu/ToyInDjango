from django.shortcuts import render
from .forms import SentenceForm
from .models import Sentence

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def capitalize(request):
    form = SentenceForm(request.POST or None) #It will post to server

    #Before validation
    context = {
        "hello_message": "Capitalize!",
        "form": form
    }

    #After validation
    if form.is_valid ():
        sentence = form.cleaned_data.get('sentence')
        sentence_cap = capital(sentence)

        context = {
            'form' : form,
            'sentence_cap': sentence_cap
        }

    return render(request, 'capitalize.html', context)

# A function that Capitalizes the first letter of each word
def capital(str):
    str = str.lower()
    str_split = str.split(" ")
    new_str = []

    for word in str_split:
        first_letter = word [0:1]
        rest_of_word = word [1:]
        first_letter_cap = first_letter.upper()
        new_word = [first_letter_cap + rest_of_word]
        new_str = new_str + new_word

    return (' '.join (new_str))

