# Generated by Django 3.1 on 2020-08-25 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200825_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='logins',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
