# Generated by Django 3.2.6 on 2021-10-28 15:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ChatBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Placements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('company', models.TextField(max_length=50)),
                ('package', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('full_name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=8)),
                ('number', models.IntegerField()),
                ('whatsapp_number', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('quote', models.TextField(max_length=50)),
                ('about_me', models.CharField(max_length=500)),
                ('graduation_year', models.IntegerField()),
                ('designation', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=200)),
                ('tools_and_techonologies', models.CharField(max_length=200)),
                ('proof', models.ImageField(upload_to=None)),
                ('offer_letter', models.ImageField(blank=True, upload_to=None)),
                ('linkedin', models.CharField(max_length=200)),
                ('socials', models.CharField(blank=True, max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
