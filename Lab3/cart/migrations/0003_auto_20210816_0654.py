# Generated by Django 3.2 on 2021-08-16 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20210815_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='overall_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Цена корзины'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='related_products', to='cart.CartProduct', verbose_name='Продукты'),
        ),
    ]
