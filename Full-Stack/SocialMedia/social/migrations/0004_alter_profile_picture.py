# Generated by Django 4.1.5 on 2023-02-07 22:23

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_alter_profile_followers_alter_profile_following_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default=pathlib.PureWindowsPath('/static/social/defaultPic.png'), upload_to=''),
        ),
    ]
