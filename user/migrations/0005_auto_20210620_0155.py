# Generated by Django 3.2.4 on 2021-06-20 01:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210618_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='love',
            name='love_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]