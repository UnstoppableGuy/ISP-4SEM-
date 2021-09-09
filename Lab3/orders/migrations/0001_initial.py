# Generated by Django 3.2 on 2021-08-21 19:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0005_alter_userprofile_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Адрес')),
                ('phone', models.CharField(blank=True, max_length=17, verbose_name='Номер телефона')),
                ('first_name', models.CharField(blank=True, max_length=40, verbose_name='Имя покупателя')),
                ('last_name', models.CharField(blank=True, max_length=40, verbose_name='Фамилия покупателя')),
                ('created', models.DateField(auto_now=True, verbose_name='Дата создания')),
                ('ready_time', models.DateField(default=django.utils.timezone.now, verbose_name='Время готовности')),
                ('status', models.CharField(choices=[('new_order', 'Новый заказ'), ('order_in_process', 'Заказ в обработке'), ('order_ready', 'Заказ готов'), ('order_done', 'Заказ выполнен')], default='new_order', max_length=20, verbose_name='Статус заказа')),
                ('orderType', models.CharField(choices=[('delivery', 'Доставка'), ('pickup', 'Самовывоз')], default='delivery', max_length=20, verbose_name='Тип заказа')),
                ('payment', models.CharField(choices=[('online', 'Онлайн оплата'), ('cash', 'Оплата наличными')], default='online', max_length=20, verbose_name='Тип оплаты')),
                ('comment', models.CharField(blank=True, max_length=255, verbose_name='Комментарий к заказу')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_orders', to='users.userprofile', verbose_name='Покупатель')),
            ],
        ),
    ]
