from django.db import models


class Mission(models.Model):
    codename = models.CharField('Codename', max_length=128)
    expansion = models.CharField('Expansion', max_length=128)
    reward = models.IntegerField('Reward')
    summary = models.CharField('Summary', max_length=400)
    duration = models.IntegerField('Duration')
    distance = models.IntegerField('Distance')
    volume = models.IntegerField('Volume')
    weight = models.IntegerField('Weight')

    class Meta:
        verbose_name = 'Mission'
        verbose_name_plural = 'List of Missions'

    def __str__(self):
        return self.codename
