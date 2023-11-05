# Generated by Django 4.2.6 on 2023-10-28 07:21

from django.db import migrations, models
import django.db.models.deletion
import shops.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=shops.models.getFileName)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0-show,1-Hidden')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('vendor', models.CharField(max_length=150)),
                ('product', models.ImageField(blank=True, null=True, upload_to=shops.models.getFileName)),
                ('quantity', models.IntegerField()),
                ('priginal_price', models.FloatField()),
                ('selling_Price', models.FloatField()),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0-show,1-Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0-default,1-trending')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.catagory')),
            ],
        ),
    ]
