# Generated by Django 3.0.8 on 2020-08-19 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day_day', '0006_auto_20200819_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routinecontent',
            name='priotiry',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Low'), (2, 'Medium'), (3, 'High'), (4, 'Very high')]),
        ),
    ]
