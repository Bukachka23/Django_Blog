import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
application = get_wsgi_application()

from django.test import TestCase
from django.urls import reverse

from ..models import User
from ..forms import SignUpForm

# Your test cases go here...



class TestSignUpView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='user1', email='user1@gmail.com', password='1234'
        )
        self.data = {
            'username': 'test',
            'email': 'test@hotmail.com',
            'password1': 'test12345',
            'password2': 'test12345'
        }

    def test_signup_returns_200(self):
        response = self.client.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)
        # Check we used correct template
        self.assertTemplateUsed(response, 'users/signup.html')

    def test_user_is_logged_in(self):
        response = self.client.post(
            reverse('users:signup'), self.data, follow=True
        )
        user = response.context.get('user')

        self.assertTrue(user.is_authenticated)

    def test_new_user_is_registered(self):
        # We can check that a user has been registered by trying to find
        # it in the database but I prefer the method with count()
        nb_old_users = User.objects.count()  # count users before a request
        self.client.post(reverse('users:signup'), self.data)
        nb_new_users = User.objects.count()  # count users after
        # make sure 1 user was added
        self.assertEqual(nb_new_users, nb_old_users + 1)

    def test_redirect_if_user_is_authenticated(self):
        # If the user is authenticated and try to access
        # the signup page, he is redirected to the home page
        login = self.client.login(email='user1@gmail.com', password='1234')
        response = self.client.get(reverse('users:signup'))

        self.assertRedirects(response, reverse('core:home'))

    def test_invalid_form(self):
        # We don't give a username
        response = self.client.post(reverse('users:signup'), {
            "email": "test@admin.com",
            "password1": "test12345",
            "password2": "test12345",
        })
        form = response.context.get('form')

        self.assertFalse(form.is_valid())
