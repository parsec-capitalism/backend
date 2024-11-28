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
        verbose_name_plural = 'Ships'

    def __str__(self):
        return self.name


class Perk(models.Model):
    slug = models.SlugField('Slug')
    name = models.CharField('Perk', max_length=255)
    num_value = models.IntegerField('Number value')
    bool_value = models.BooleanField('Boolean value')

    class Meta:
        verbose_name = 'Perk'
        verbose_name_plural = 'Perks'

    def __str__(self):
        return self.name


class UserShip(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='player',
    )
    ship = models.ForeignKey(
        Ship,
        on_delete=models.CASCADE,
        related_name='ships',
    )
    on_mission = models.BooleanField(verbose_name='On mission', default=False)

    class Meta:
        verbose_name = 'Players ship'
        verbose_name_plural = 'Players ships'

    def __str__(self):
        return f'{self.user} - {self.ship}'
