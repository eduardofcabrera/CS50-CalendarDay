# Generated by Django 3.0.8 on 2020-08-19 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day_day', '0004_auto_20200819_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routinecontent',
            name='date_finish',
            field=models.DateTimeField(blank=True, verbose_name='date finish'),
        ),
    ]
