# Generated by Django 4.2.4 on 2023-09-04 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_products_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_best_seller',
            field=models.BooleanField(default=False),
        ),
    ]