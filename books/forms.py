from django import forms
from .models import Comment, Books
from django.utils.translation import gettext as _


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'star', 'recommend']


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'text', 'author', 'price', 'image']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': _('search for book')}))


