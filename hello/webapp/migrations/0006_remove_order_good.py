# Generated by Django 3.1.7 on 2021-04-26 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='good',
        ),
    ]
