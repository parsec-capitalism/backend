# Generated by Django 5.0.6 on 2025-02-17 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ships', '0012_rename_amount_shipperks_default_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usershipperks',
            name='owned_amount',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Amount'),
        ),
    ]
