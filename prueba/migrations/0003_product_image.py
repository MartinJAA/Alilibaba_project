# Generated by Django 4.1.3 on 2022-11-23 03:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0002_product_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
