# Generated by Django 2.0.2 on 2018-12-27 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistencias', '0007_auto_20180410_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='rgpd',
            field=models.BooleanField(default=False),
        ),
    ]
