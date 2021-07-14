# Generated by Django 3.0.5 on 2020-05-12 20:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0009_auto_20200512_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_receiver', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 5, 12, 21, 28, 30, 839880)),
        ),
        migrations.AlterField(
            model_name='report',
            name='time',
            field=models.TimeField(default='20:28', max_length=5),
        ),
    ]
