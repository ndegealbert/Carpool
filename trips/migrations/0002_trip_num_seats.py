# Generated by Django 3.0.7 on 2020-06-16 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='num_seats',
            field=models.IntegerField(default=1, help_text='Number of seats available', verbose_name='Number of seats'),
        ),
    ]
