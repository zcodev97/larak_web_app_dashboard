# Generated by Django 4.2.6 on 2023-10-30 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_user_user_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]