# Generated by Django 2.2.1 on 2019-05-21 03:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0004_auto_20190521_0525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compaign',
            name='end_date',
            field=models.DateField(default=datetime.date(2019, 5, 28)),
        ),
    ]
