# Generated by Django 4.0 on 2024-01-20 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=25, verbose_name='название товара')),
                ('price', models.FloatField(verbose_name='цена')),
                ('description', models.TextField(verbose_name='описание товара')),
                ('image', models.ImageField(upload_to='goods/', verbose_name='картинка товара')),
                ('amount', models.PositiveIntegerField(verbose_name='кол-во товара')),
                ('activity_flag', models.CharField(choices=[('a', 'Aктивный'), ('i', 'Стоп-лист')], default='i', max_length=1, verbose_name='флаг активности')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
                'db_table': 'good',
            },
        ),
        migrations.CreateModel(
            name='GoodCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good_num', models.PositiveIntegerField(default=1, verbose_name='кол-во')),
                ('payment_flag', models.CharField(choices=[('p', 'Оплачен'), ('n', 'Не оплачен')], default='n', max_length=1, verbose_name='статус оплаты')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_shop.good', verbose_name='товар')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'корзина',
                'verbose_name_plural': 'корзины',
                'db_table': 'good2cart',
            },
        ),
        migrations.CreateModel(
            name='GoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='категория товара')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='название магазина')),
                ('log', models.ImageField(upload_to='shop_logo/', verbose_name='логотип магазина')),
            ],
            options={
                'verbose_name': 'магазин',
                'verbose_name_plural': 'магазины',
                'db_table': 'shop',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField(default=0, verbose_name='баланс')),
                ('purchase_amount', models.FloatField(default=0, verbose_name='сумма покупок')),
                ('status_flag', models.CharField(choices=[('new', 'Новичок'), ('adv', 'Продвинутый'), ('exp', 'Эксперт')], default='new', max_length=3, verbose_name='статус')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'профиль',
                'verbose_name_plural': 'профили',
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='дата заказа')),
                ('amount', models.FloatField(default=0, verbose_name='общая стоимость')),
                ('cart_good', models.ManyToManyField(to='app_shop.GoodCart', verbose_name='товар из корзины')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
                'db_table': 'order',
            },
        ),
        migrations.AddField(
            model_name='good',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_shop.goodcategory', verbose_name='категория'),
        ),
        migrations.AddField(
            model_name='good',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='app_shop.shop', verbose_name='магазин'),
        ),
    ]
