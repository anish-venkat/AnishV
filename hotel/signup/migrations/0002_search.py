# Generated by Django 2.2.3 on 2019-11-06 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lcity', models.CharField(max_length=50)),
                ('lguests', models.IntegerField()),
                ('larrival', models.CharField(max_length=50)),
                ('ldeparture', models.CharField(max_length=50)),
            ],
        ),
    ]
