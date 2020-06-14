from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Card(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='card_set')
    card_name = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.owner},{self.card_name}'
