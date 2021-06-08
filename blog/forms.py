from django import forms
from django.forms import widgets
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(attrs={
        'type':"text",
        'class':"form-control mr-3",
        'placeholder':"Add comment",
    }), label='')

    class Meta:
        model = Comment
        fields = ('body',)

# class SearchForm(forms.Form):
#     query = forms.CharField()
