from django.contrib.auth.models import AbstractUser
from django.db import models

from static.game_config import STARTER_DATACOINS


class Player(AbstractUser):
    datacoins = models.PositiveIntegerField('Datacoins', default=STARTER_DATACOINS)

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __str__(self):
        return f'{self.username}'
