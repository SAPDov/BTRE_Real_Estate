# Generated by Django 3.2.6 on 2021-08-31 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.CharField(max_length=200)),
                ('listing_id', models.IntegerField()),
                ('user_id', models.IntegerField(blank=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.TextField(blank=True)),
                ('inquiry_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
