# Generated by Django 2.0.2 on 2018-04-04 14:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistencias', '0004_auto_20180404_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistencia',
            name='data',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
