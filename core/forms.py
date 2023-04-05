from django import forms
from .models import Comment

# A subclass of ModelForm that provides a default form for editing model instances.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')