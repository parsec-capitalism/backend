# Generated by Django 5.0.6 on 2024-11-22 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ships', '0006_perk'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perk',
            options={'verbose_name': 'Perk', 'verbose_name_plural': 'Perks'},
        ),
        migrations.AlterModelOptions(
            name='ship',
            options={'verbose_name': 'Ship', 'verbose_name_plural': 'Ships'},
        ),
        migrations.AlterModelOptions(
            name='usership',
            options={'verbose_name': 'Players ship', 'verbose_name_plural': 'Players ships'},
        ),
    ]
