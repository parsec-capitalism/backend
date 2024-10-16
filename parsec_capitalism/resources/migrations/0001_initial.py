# Generated by Django 5.0.6 on 2024-10-16 16:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datacoin', models.PositiveIntegerField(verbose_name='Datacoins')),
                ('quantium', models.PositiveIntegerField(verbose_name='Quantium')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Player Resource',
                'verbose_name_plural': 'Players Resources',
            },
        ),
    ]
