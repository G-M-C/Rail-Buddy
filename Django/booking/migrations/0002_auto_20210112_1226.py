# Generated by Django 3.1.4 on 2021-01-12 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='station_name',
            field=models.CharField(default='ernakulam', max_length=100),
        ),
    ]
