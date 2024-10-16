from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UserResource(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datacoin = models.PositiveIntegerField(verbose_name='Datacoins')
    quantium = models.PositiveIntegerField(verbose_name='Quantium')

    class Meta:
        verbose_name = 'Player Resource'
        verbose_name_plural = 'Players Resources'

    def __str__(self):
        return f'{self.user}:{self.datacoin} {self.datacoin}'
