# Generated by Django 3.2.18 on 2024-01-17 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loto', '0003_alter_user_cellphone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='cellphone',
        ),
    ]