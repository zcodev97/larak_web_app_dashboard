# Generated by Django 4.2.6 on 2023-10-26 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.ForeignKey(default='875b469b-d0e2-4108-8e7a-bfe40b8c81fc', on_delete=django.db.models.deletion.CASCADE, to='core.usertype'),
            preserve_default=False,
        ),
    ]