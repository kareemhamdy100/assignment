# Generated by Django 2.2.1 on 2019-05-21 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0002_auto_20190521_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compaign',
            name='end_date',
            field=models.DateField(default=1),
        ),
    ]