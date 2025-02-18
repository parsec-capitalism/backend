from django.db import models


class Mission(models.Model):
    expansion = models.CharField('Expansion', max_length=128)
    name = models.CharField('Name', max_length=128)
    summary = models.CharField('Summary', max_length=400)
    reward = models.IntegerField('Reward')
    duration = models.IntegerField('Duration')
    distance = models.IntegerField('Distance')
    volume = models.IntegerField('Volume')

    class Meta:
        verbose_name = 'Mission'
        verbose_name_plural = 'List of Missions'

    def __str__(self):
        return self.name
