# Generated by Django 4.2.5 on 2023-10-30 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userprofile_delete_media'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
