# Generated by Django 4.0 on 2023-12-09 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='author',
        ),
    ]
