from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractUser
import random

def generate_random_int():
    """Returns a random integer between 1 and 100"""
    return random.randint(1, 100)


class User(AbstractUser):
    """
    A new User model that extends from the `User` django base model
    """
    date_of_birth = models.DateField(null=True)
    random_number = models.IntegerField(default=generate_random_int)

    def get_absolute_url(self):
        """Returns an absolute url for the detail view of the model"""
        return reverse('user-detail', kwargs={'pk': self.pk})
