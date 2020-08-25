# Generated by Django 3.1 on 2020-08-25 17:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20200825_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='time_joined',
        ),
        migrations.AddField(
            model_name='user',
            name='joined_time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='joined time'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='joined_date',
            field=models.DateField(auto_now_add=True, verbose_name='joined date'),
        ),
    ]
