# Generated by Django 4.1.5 on 2023-02-15 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_productincart_totalcost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Waiting for order confirmation', 'Waiting for order confirmation'), ('Shipping', 'Shipping'), ('On Delivery', 'On Delivery'), ('Delivered', 'Delivered'), ('Problem with Transit', 'Problem with Transit')], default='Waiting for order confirmation', max_length=50),
        ),
    ]
