# Generated by Django 3.2.3 on 2021-05-18 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locker',
            name='featured',
            field=models.CharField(choices=[('Small', 'S'), ('Medium', 'M'), ('Large', 'L')], max_length=6),
        ),
    ]
