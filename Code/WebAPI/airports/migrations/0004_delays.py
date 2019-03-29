# Generated by Django 2.1.7 on 2019-03-23 22:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airports', '0003_auto_20190323_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airport', models.CharField(max_length=3)),
                ('carrier', models.CharField(max_length=3)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('late_aircraft', models.IntegerField()),
                ('weather', models.IntegerField()),
                ('security', models.IntegerField()),
                ('nas', models.IntegerField()),
                ('carrier_delay', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Delays',
            },
        ),
    ]