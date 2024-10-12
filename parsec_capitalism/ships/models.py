from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Ship(models.Model):
    title = models.CharField(max_length=128, verbose_name='Name of the ship')
    cost = models.IntegerField(verbose_name='Price')
    size = models.IntegerField(verbose_name='Size')
    slug = models.SlugField(verbose_name='Slug for internal use')

    class Meta:
        verbose_name = 'Ship Model'
        verbose_name_plural = 'List of Ship Models'

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
        return f'{self.user} {self.ship}'
