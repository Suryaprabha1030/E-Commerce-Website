# Generated by Django 4.2.6 on 2023-10-29 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product',
            new_name='product_image',
        ),
    ]
