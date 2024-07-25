# Generated by Django 5.0.7 on 2024-07-20 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EuphoricApp', '0002_remove_products_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='image',
        ),
        migrations.RemoveField(
            model_name='products',
            name='name',
        ),
        migrations.RemoveField(
            model_name='products',
            name='price',
        ),
        migrations.AddField(
            model_name='products',
            name='product_title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]