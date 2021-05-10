from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Deck(TimeStampedModel):
    THEMES = [
        ("black", "black"),
        ("beige", "beige"),
        ("blood", "blood"),
        ("league", "league"),
        ("moon", "moon"),
        ("night", "night"),
        ("serif", "serif"),
        ("simple", "simple"),
        ("sky", "sky"),
        ("solarized", "solarized"),
        ("white", "white"),
    ]

    title = models.TextField()
    text = models.TextField()
    theme = models.CharField(max_length=256, choices=THEMES, default="simple")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
