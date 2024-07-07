from django.db import models

# Create your models here.


class Ships(models.Model):
    title = models.CharField(max_length=128, verbose_name='Name of the ship')
    cost = models.IntegerField(verbose_name='Price')
    size = models.IntegerField(verbose_name='Size')
    slug = models.SlugField(verbose_name='Slug for internal use')

    class Meta:
        verbose_name = 'Ship Model'
        verbose_name_plural = 'List of Ship Models'

    def __str__(self):
        return self.title
