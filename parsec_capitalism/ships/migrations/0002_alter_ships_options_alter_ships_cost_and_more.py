# Generated by Django 5.0.6 on 2024-07-07 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ships', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ships',
            options={'verbose_name': 'Ship Model', 'verbose_name_plural': 'List of Ship Models'},
        ),
        migrations.AlterField(
            model_name='ships',
            name='cost',
            field=models.IntegerField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='ships',
            name='size',
            field=models.IntegerField(verbose_name='Size'),
        ),
        migrations.AlterField(
            model_name='ships',
            name='slug',
            field=models.SlugField(verbose_name='Slug for internal use'),
        ),
        migrations.AlterField(
            model_name='ships',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Name of the ship'),
        ),
    ]
