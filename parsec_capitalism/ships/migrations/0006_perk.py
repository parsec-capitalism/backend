# Generated by Django 5.0.6 on 2024-11-21 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ships', '0005_alter_ship_options_rename_title_ship_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('name', models.CharField(max_length=255, verbose_name='Perk')),
                ('num_value', models.IntegerField(verbose_name='Number value')),
                ('bool_value', models.BooleanField(verbose_name='Boolean value')),
            ],
            options={
                'verbose_name': 'Perk',
                'verbose_name_plural': 'List of Perks',
            },
        ),
    ]
