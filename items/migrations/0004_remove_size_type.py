# Generated by Django 4.2.6 on 2023-10-24 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_size_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='size',
            name='type',
        ),
    ]