from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Profile

@receiver(pre_save, sender=User)
def set_username(sender, instance, **kwargs):
    if not instance.username:
        username = f'{instance.first_name}_{instance.last_name}'.lower()
        counter = 1
        max_attempts = 100  # Set a maximum number of attempts to avoid infinite loop

        while User.objects.filter(username=username).exists() and counter <= max_attempts:
            username = f'{instance.first_name}_{instance.last_name}_{counter}'.lower()
            counter += 1

        # If the loop reaches the maximum attempts, you may want to handle it appropriately.
        if counter > max_attempts:
            raise ValueError("Unable to generate a unique username.")

        instance.username = username
