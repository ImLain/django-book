from django import forms
from django.forms import ModelForm

from posts.models import BookPost


class DateInput(forms.DateInput):
    input_type = 'date'

class BookForm(ModelForm):    
    class Meta:
        model = BookPost
        fields = ['title', 'book_author', 'content','created_on', 'thumbnail', 'score']
        widgets = {
            'created_on': DateInput(),
            'score': forms.NumberInput(attrs={'class': 'hidden'})
        }

class BookFormEdit(ModelForm):
    class Meta:
        model = BookPost
        fields = ['title', 'book_author', 'content','created_on', 'published', 'thumbnail', 'score']
        widgets = {
            'created_on': DateInput(),
            'score': forms.NumberInput(attrs={'class': 'hidden'})
        }