# Generated by Django 2.0.8 on 2018-11-30 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20181130_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='locked',
            field=models.BooleanField(default=False),
        ),
    ]
