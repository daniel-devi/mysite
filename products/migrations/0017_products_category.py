# Generated by Django 4.2.4 on 2023-09-04 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_remove_products_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ManyToManyField(to='products.category'),
        ),
    ]
