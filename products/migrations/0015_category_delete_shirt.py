# Generated by Django 4.2.4 on 2023-09-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_address_brand_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Shirt',
        ),
    ]
