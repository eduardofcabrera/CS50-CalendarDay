# Generated by Django 3.0.8 on 2020-08-19 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('day_day', '0005_auto_20200819_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_routine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='day_day.Routine'),
        ),
    ]