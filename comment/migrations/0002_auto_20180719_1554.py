# Generated by Django 2.0.7 on 2018-07-19 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_time',
            new_name='create_time',
        ),
    ]
