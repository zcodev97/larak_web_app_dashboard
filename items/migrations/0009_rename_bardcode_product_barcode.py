# Generated by Django 4.2.6 on 2023-10-24 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_rename_price_product_cost_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='bardcode',
            new_name='barcode',
        ),
    ]