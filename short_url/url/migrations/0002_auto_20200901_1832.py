# Generated by Django 3.1 on 2020-09-01 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allurl',
            name='short_url',
            field=models.CharField(blank=True, max_length=6, unique=True),
        ),
    ]
