# Generated by Django 4.2.6 on 2023-10-26 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0004_alter_cart_cart_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='created_by',
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(default='45e2a8ae-b2f4-4380-81a2-7e06014aa202', on_delete=django.db.models.deletion.CASCADE, to='orders.cart'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver', to=settings.AUTH_USER_MODEL),
        ),
    ]
