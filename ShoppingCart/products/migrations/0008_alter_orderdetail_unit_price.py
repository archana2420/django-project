# Generated by Django 4.1.6 on 2023-02-13 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_order_order_id_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='unit_price',
            field=models.IntegerField(),
        ),
    ]