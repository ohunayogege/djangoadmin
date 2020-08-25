# Generated by Django 3.1 on 2020-08-25 15:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_logincount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logincount',
            name='log_count',
        ),
        migrations.AddField(
            model_name='logincount',
            name='browser',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='logincount',
            name='date_sent',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date Sent'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logincount',
            name='ip_address',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='logincount',
            name='time_sent',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Time Sent'),
            preserve_default=False,
        ),
    ]