# Generated by Django 2.0.8 on 2018-11-26 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='race',
            old_name='race_day',
            new_name='day',
        ),
        migrations.RenameField(
            model_name='race',
            old_name='race_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='race',
            old_name='race_time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='runner',
            old_name='horse_name',
            new_name='name',
        ),
    ]
