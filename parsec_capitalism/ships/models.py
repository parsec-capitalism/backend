from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Perk(models.Model):
    class PerkTypes(models.TextChoices):
        PERMANENT = 'PERM', 'Permanent'
        DISPOSABLE = 'DISP', 'Disposable'
        ONE_TIMER = '1TIME', 'One-timer'
        RENT = 'RENT', 'Rent'

    name = models.CharField('Perk', max_length=255)
    type = models.CharField(
        'Perk type',
        max_length=5,
        choices=PerkTypes.choices,
        default=PerkTypes.PERMANENT,
    )
    description = models.TextField('Description')
    ad_text = models.TextField('Ad Text')

    class Meta:
        verbose_name = 'Perk'
        verbose_name_plural = 'Perks'

    def __str__(self):
        return self.name


class Ship(models.Model):
    slug = models.SlugField('Slug for internal use')
    name = models.CharField('Name of the ship', max_length=128)
    price = models.PositiveSmallIntegerField('Price')
    range = models.PositiveSmallIntegerField('Range')
    cargo_hold = models.PositiveSmallIntegerField('Cargo Hold')
    perks = models.ManyToManyField(
        Perk,
        on_delete=models.CASCADE,
        related_name='ships_with_perks',
        verbose_name='Perks',
    )

    class Meta:
        verbose_name = 'Ship'
        verbose_name_plural = 'Ships'

    def __str__(self):
        return self.name


class UserShip(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_ships',
    )
    ship = models.ForeignKey(
        Ship,
        on_delete=models.CASCADE,
        related_name='ship_users',
    )
    on_mission = models.BooleanField('On mission', default=False)

    class Meta:
        verbose_name = 'Players ship'
        verbose_name_plural = 'Players ships'

    def __str__(self):
        return f'{self.user} - {self.ship}'
