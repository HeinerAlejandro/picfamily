# Generated by Django 2.1.4 on 2019-04-26 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20190426_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='posts',
            field=models.IntegerField(default=10),
        ),
    ]