# Generated by Django 3.1.4 on 2021-01-12 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='berth',
            field=models.CharField(default='Upper Berth', max_length=20),
        ),
    ]
