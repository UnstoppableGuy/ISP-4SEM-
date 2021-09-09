# Generated by Django 3.2 on 2021-08-21 20:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210815_1701'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ready_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата готовности'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('overall_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена товара')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_order', to='orders.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Продукт')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='related_products', to='orders.OrderItem', verbose_name='Продукты'),
        ),
    ]
