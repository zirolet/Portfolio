# Generated by Django 4.1.5 on 2023-02-08 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0021_alter_comment_options_comment_datetime_comment_entry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='picture',
        ),
    ]
