# Generated by Django 2.2.3 on 2019-11-06 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_search'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='larrival',
            field=models.DateField(max_length=50),
        ),
        migrations.AlterField(
            model_name='search',
            name='ldeparture',
            field=models.DateField(max_length=50),
        ),
    ]
