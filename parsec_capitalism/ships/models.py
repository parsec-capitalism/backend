from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Ship(models.Model):
    slug = models.SlugField(verbose_name='Slug for internal use')
    name = models.CharField(max_length=128, verbose_name='Name of the ship')
    price = models.IntegerField(verbose_name='Price')
    cargo_weight = models.IntegerField(verbose_name='Cargo Weight')
    cargo_volume = models.IntegerField(verbose_name='Cargo Volume')
    range = models.IntegerField(verbose_name='Range')

    class Meta:
        verbose_name = 'Ship'
        verbose_name_plural = 'List of Ships'

    def __str__(self):
        return self.title


class UserShip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    on_mission = models.BooleanField(verbose_name='On mission', default=False)

    class Meta:
        verbose_name = 'Ships that Players Have'
        verbose_name_plural = 'List of Ships per Player'

    def __str__(self):
        return f'{self.user} - {self.ship}'
