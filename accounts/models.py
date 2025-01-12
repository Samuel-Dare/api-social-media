from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    # followers = models.ManyToManyField(
    #     'self',
    #     symmetrical=False,
    #     related_name='following',  # Reverse relationship works here
    #     blank=True
    # )
    following = models.ManyToManyField(
    'self',
    symmetrical=False,  # If False, users won't follow each other automatically
    related_name='followers',  # Reverse relationship to get the users following a given user
    blank=True
    )

    def __str__(self):
        return self.username