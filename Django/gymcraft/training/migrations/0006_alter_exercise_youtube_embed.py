# Generated by Django 3.2.12 on 2024-05-03 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0005_auto_20240503_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='youtube_embed',
            field=models.TextField(null=True),
        ),
    ]