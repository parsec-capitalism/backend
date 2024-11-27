from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class Player(AbstractUser):
    def add_starter_resources(self):
        if not hasattr(self, 'resource'):
            Resource.objects.create(user=self, datacoin=100)

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            self.add_starter_resources()


User = get_user_model()


class Resource(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    datacoin = models.PositiveIntegerField('Datacoins')

    class Meta:
        verbose_name = 'Player Resource'
        verbose_name_plural = 'Players Resources'

    def __str__(self):
        return f'{self.user} - {self.datacoin} DCs'
