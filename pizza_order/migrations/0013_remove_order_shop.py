# Generated by Django 3.2.13 on 2022-09-01 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_order', '0012_order_shop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shop',
        ),
    ]
