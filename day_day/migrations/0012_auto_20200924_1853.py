# Generated by Django 3.0.8 on 2020-09-24 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day_day', '0011_auto_20200819_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advice',
            name='active',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='place',
        ),
        migrations.RemoveField(
            model_name='task',
            name='finished',
        ),
        migrations.AddField(
            model_name='routinecontent',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]