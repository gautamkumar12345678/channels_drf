# Generated by Django 3.2.13 on 2022-08-09 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_order', '0002_auto_20220809_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartpizza',
            name='total_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.IntegerField(default=0),
        ),
    ]
