# Generated by Django 2.0.7 on 2018-07-31 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180731_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('visitor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.Visitor')),
                ('iflike', models.IntegerField(default=0)),
            ],
            bases=('blog.visitor',),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visitor',
            name='user_agent',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
