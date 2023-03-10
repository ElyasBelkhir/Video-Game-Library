# Generated by Django 4.1.1 on 2022-10-01 23:11

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='gameDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='gameRating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='room',
            name='gameTitle',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
