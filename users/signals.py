from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, Profile

# A decorator that registers a function to be called when a particular signal is sent.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

