from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


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


class PlayerMission(models.Model):
    class MissionStatus(models.TextChoices):
        IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
        COMPLETED = 'COMPLETED', 'Completed'
        FAILED = 'FAILED', 'Failed'

    player = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='player_missions',
        verbose_name='Player'
    )
    mission = models.ForeignKey(
        Mission,
        on_delete=models.CASCADE,
        related_name='mission_attempts',
        verbose_name='Mission'
    )
    ship = models.ForeignKey(
        'ships.UserShip',
        on_delete=models.CASCADE,
        related_name='ship_missions',
        verbose_name='Ship Used'
    )
    start_time = models.DateTimeField('Start Time', auto_now_add=True)
    finish_time = models.DateTimeField('Finish Time', null=True, blank=True)
    reward = models.IntegerField('Actual Reward')
    status = models.CharField(
        'Mission Status',
        max_length=20,
        choices=MissionStatus.choices,
        default=MissionStatus.IN_PROGRESS
    )

    class Meta:
        verbose_name = 'Player Mission'
        verbose_name_plural = 'Player Missions'
        ordering = ['-start_time']

    def __str__(self):
        return f'{self.player.username} - {self.mission.name} ({self.status})'
