# Generated by Django 4.1.6 on 2023-02-11 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.URLField(default='https://picsum.photos/200', max_length=100000),
        ),
    ]
