# Generated by Django 3.2.6 on 2021-10-28 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='whatsapp_number',
            field=models.IntegerField(blank=True),
        ),
    ]
