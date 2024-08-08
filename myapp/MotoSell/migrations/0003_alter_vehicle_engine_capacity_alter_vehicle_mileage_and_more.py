# Generated by Django 5.0.7 on 2024-08-08 11:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MotoSell', '0002_vehicle_delete_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='engine_capacity',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='mileage',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(1500000)]),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='power',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2000)]),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='year',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2025)]),
        ),
    ]