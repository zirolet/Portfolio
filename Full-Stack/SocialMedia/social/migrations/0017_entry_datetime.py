# Generated by Django 4.1.5 on 2023-02-08 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0016_alter_entry_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='dateTime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
