# Generated by Django 3.1 on 2020-09-03 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0003_auto_20200903_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allurl',
            name='long_url',
            field=models.CharField(max_length=200),
        ),
    ]
