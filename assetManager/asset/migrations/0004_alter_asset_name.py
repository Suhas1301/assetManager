# Generated by Django 5.2.4 on 2025-07-25 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_alter_asset_entity_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
