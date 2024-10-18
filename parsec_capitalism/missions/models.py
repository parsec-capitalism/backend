from django.db import models

# Create your models here.


class Missions(models.Model):
    title = models.CharField(max_length=128, verbose_name='Mission name')

    class Meta:
        verbose_name = 'Mission'
        verbose_name_plural = 'List of Missions'

    def __str__(self):
        return self.title
