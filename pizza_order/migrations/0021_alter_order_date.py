# Generated by Django 3.2.13 on 2022-09-22 19:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_order', '0020_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 22, 19, 3, 25, 293650, tzinfo=utc)),
        ),
    ]
