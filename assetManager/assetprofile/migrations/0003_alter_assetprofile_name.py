# Generated by Django 5.2.4 on 2025-07-25 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetprofile', '0002_alter_assetprofile_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetprofile',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
