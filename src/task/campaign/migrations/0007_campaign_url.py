# Generated by Django 2.2.1 on 2019-05-21 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0006_auto_20190521_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='url',
            field=models.TextField(default='hello', max_length=300),
            preserve_default=False,
        ),
    ]