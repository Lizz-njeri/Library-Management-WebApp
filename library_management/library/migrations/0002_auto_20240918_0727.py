# Generated by Django 3.2 on 2024-09-18 04:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='membership_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='member',
            name='phone_number',
            field=models.CharField(default='+25471000000', max_length=20),
        ),
    ]
