# Generated by Django 2.0.8 on 2018-11-27 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='odds',
            field=models.CharField(max_length=50),
        ),
    ]
