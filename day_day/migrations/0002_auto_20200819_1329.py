# Generated by Django 3.0.8 on 2020-08-19 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('day_day', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_routine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='day_day.Routine'),
        ),
    ]
