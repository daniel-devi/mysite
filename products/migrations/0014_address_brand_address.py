# Generated by Django 4.2.4 on 2023-09-04 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_shirt_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=1024, null=True)),
                ('zipCode', models.SlugField(null=True)),
                ('city', models.PositiveIntegerField(null=True)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='brand',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Products', to='products.address'),
        ),
    ]
