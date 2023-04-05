from django.db import models
from django.contrib.auth.models import AbstractUser


# A subclass of AbstractUser that provides a default user model.
class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]


# A subclass of Model that provides a default implementation of a model, including the basic fields and behaviors of the model.
class Profile(models.Model):
    about_me = models.TextField()
    image = models.ImageField(upload_to='profile_image', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username