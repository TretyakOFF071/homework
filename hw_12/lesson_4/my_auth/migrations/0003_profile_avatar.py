# Generated by Django 4.0 on 2024-01-22 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_auth', '0002_record_imagesrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]
