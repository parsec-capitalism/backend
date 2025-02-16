# Generated by Django 5.0.6 on 2025-02-16 19:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ships', '0003_remove_ship_perks'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShipPerks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(verbose_name='Amount')),
                ('perk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ships.perk')),
                ('ship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ships.ship')),
            ],
        ),
        migrations.AddField(
            model_name='ship',
            name='perks',
            field=models.ManyToManyField(through='ships.ShipPerks', to='ships.perk'),
        ),
    ]
