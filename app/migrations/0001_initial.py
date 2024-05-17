# Generated by Django 5.0.6 on 2024-05-17 12:11

import app.models
import django.db.models.deletion
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
                ('name', models.CharField(max_length=32)),
                ('logo', models.ImageField(upload_to=app.models.get_img_upload_path)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('link', models.TextField(blank=True, null=True)),
                ('logo', models.BinaryField(blank=True, editable=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('link', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgtitle', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.project')),
            ],
        ),
    ]