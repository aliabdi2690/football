from django import forms
from .models import Comment

class CommentForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea)
