# Generated by Django 4.2.6 on 2023-10-30 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0015_banner_to_product'),
        ('orders', '0005_remove_order_created_by_order_cart_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_items',
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_items',
            field=models.ManyToManyField(related_name='carts', to='items.product'),
        ),
    ]