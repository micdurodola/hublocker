# Generated by Django 3.2.3 on 2021-05-18 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_locker_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locker',
            name='featured',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1),
        ),
    ]