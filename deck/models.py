from django.contrib.auth.models import User
from django.db import models

from django_extensions.db.models import TimeStampedModel


class Deck(TimeStampedModel):
    title = models.TextField()
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
