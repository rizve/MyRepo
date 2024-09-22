from django import forms
from .models import Book
from tinymce.widgets import TinyMCE

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date','content']

        # widgets = {
        #     'content': TinyMCE(),
        # }
        # widgets = {'content': TinyMCE(attrs={'cols': 80, 'rows': 30})}
        widgets = {
            'content': TinyMCE(),
        }
