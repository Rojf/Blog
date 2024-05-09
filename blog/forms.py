from django import forms

from blog.repositories import Repository


class CommentForm(forms.Form):
    body = forms.CharField()
    author = forms.ModelChoiceField(queryset=Repository.UserRepository.all())


class EmailPostForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Repository.UserRepository.all())
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class SearchForm(forms.Form):
    query = forms.CharField()
