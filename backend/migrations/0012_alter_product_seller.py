# Generated by Django 4.0.6 on 2022-07-09 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_alter_product_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
