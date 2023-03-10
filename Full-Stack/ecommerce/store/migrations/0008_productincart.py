# Generated by Django 4.1.5 on 2023-02-14 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_order_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='productInCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.profile')),
            ],
        ),
    ]
