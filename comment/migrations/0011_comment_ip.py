# Generated by Django 2.0.7 on 2018-07-31 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0010_auto_20180727_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='ip',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
