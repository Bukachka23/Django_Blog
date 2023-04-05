from django import forms
from django.contrib.auth.forms import UserCreationForm

from.models import User


# A subclass of UserCreationForm that provides a default form for creating a new user.
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")


# A subclass of Form that provides a default form for logging in a user.
class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()


# A subclass of Form that provides a default form for editing a user's profile.
class EditProfileForm(forms.Form):
    username = forms.CharField()
    about_me = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField(required=False)

    # A function that returns the cleaned data.
    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username


    def clean_username(self):
        """
        This function throws an exception if the username has already been
        taken by another user
        """
        username = self.cleaned_data['username']
        if username != self.original_username:
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError(
                    'A user with that username already exists.')
        return username

# A subclass of Form that provides a default form for searching a user.
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Search', 'class': 'form-control mr-sm-2'}))
