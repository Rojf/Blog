from django import forms

from blog.repositories import Repository
from blog.models import Comment


class _CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'author']


class CommentForm(forms.Form):
    body = forms.CharField()
    # author = forms.ModelChoiceField(queryset=get_user())
    author = forms.ModelChoiceField(queryset=Repository.UserRepository.all())


class EmailPostForm(forms.Form):
    # author = forms.ModelChoiceField(queryset=get_user())
    author = forms.ModelChoiceField(queryset=Repository.UserRepository.all())
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class SearchForm(forms.Form):
    query = forms.CharField()
