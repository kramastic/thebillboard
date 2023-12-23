# Generated by Django 4.2.6 on 2023-12-09 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('name', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Действие')),
                ('name_adv', models.CharField(max_length=40)),
                ('name_catalog', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Действие',
                'verbose_name_plural': 'Действия',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Тип недвижимости')),
                ('rus_name', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Тип недвижимости',
                'verbose_name_plural': 'Типы недвижимости',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес*')),
                ('specification', models.TextField(verbose_name='Описание*')),
                ('total_area', models.FloatField(verbose_name='Общая площадь*')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотографии')),
                ('online_show', models.CharField(blank=True, max_length=20, null=True, verbose_name='Онлайн показ')),
                ('price', models.CharField(max_length=15, verbose_name='Цена*')),
                ('transaction_terms', models.CharField(blank=True, max_length=100, null=True, verbose_name='Условия сделки')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('room_in_total', models.SmallIntegerField(verbose_name='Всего комнат в квартире*')),
                ('building_type', models.CharField(blank=True, max_length=20, null=True, verbose_name='Тип дома')),
                ('floor', models.SmallIntegerField(verbose_name='Этаж*')),
                ('max_floor', models.SmallIntegerField(verbose_name='Количество этажей в доме*')),
                ('video_link', models.CharField(blank=True, max_length=20, null=True, verbose_name='Ссылка на видео')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bboard.action', verbose_name='Действие')),
                ('item_type', models.ForeignKey(default='room', editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='room', to='bboard.type', verbose_name='Тип объекта*')),
            ],
            options={
                'verbose_name': 'Комната',
                'verbose_name_plural': 'Комнаты',
                'ordering': ['-time_update'],
            },
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес*')),
                ('specification', models.TextField(verbose_name='Описание*')),
                ('total_area', models.FloatField(verbose_name='Общая площадь*')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотографии')),
                ('online_show', models.CharField(blank=True, max_length=20, null=True, verbose_name='Онлайн показ')),
                ('price', models.CharField(max_length=15, verbose_name='Цена*')),
                ('transaction_terms', models.CharField(blank=True, max_length=100, null=True, verbose_name='Условия сделки')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('parking_type', models.CharField(choices=[(None, 'Выбрать'), ('Гараж', 'Гараж'), ('Машиноместо', 'Машиноместо')], max_length=15, verbose_name='Гараж/Машиноместо*')),
                ('video_link', models.CharField(blank=True, max_length=20, null=True, verbose_name='Ссылка на видео')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bboard.action', verbose_name='Действие')),
                ('item_type', models.ForeignKey(default='parking', editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='parking', to='bboard.type', verbose_name='Тип объекта')),
            ],
            options={
                'verbose_name': 'Гараж/Машиноместо',
                'verbose_name_plural': 'Гаражи/Машиноместа',
                'ordering': ['time_update'],
            },
        ),
        migrations.CreateModel(
            name='Land_plot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес*')),
                ('specification', models.TextField(verbose_name='Описание*')),
                ('total_area', models.FloatField(verbose_name='Общая площадь*')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотографии')),
                ('price', models.CharField(max_length=15, verbose_name='Цена*')),
                ('transaction_terms', models.CharField(blank=True, max_length=100, null=True, verbose_name='Условия сделки')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('video_link', models.CharField(blank=True, max_length=20, null=True, verbose_name='Ссылка на видео')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bboard.action', verbose_name='Действие')),
                ('item_type', models.ForeignKey(default='land_plot', editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='land_plot', to='bboard.type', verbose_name='Тип объекта*')),
            ],
            options={
                'verbose_name': 'Земельный участок',
                'verbose_name_plural': 'Земельные участки',
                'ordering': ['-time_update'],
            },
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес*')),
                ('specification', models.TextField(verbose_name='Описание*')),
                ('total_area', models.FloatField(verbose_name='Общая площадь*')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотографии')),
                ('online_show', models.CharField(blank=True, max_length=20, null=True, verbose_name='Онлайн показ')),
                ('price', models.CharField(max_length=15, verbose_name='Цена*')),
                ('transaction_terms', models.CharField(blank=True, max_length=100, null=True, verbose_name='Условия сделки')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('apartment_type', models.CharField(choices=[(None, 'Выбрать'), ('Квартира', 'Квартира'), ('Апартаменты', 'Апартаменты')], max_length=15, verbose_name='Квартира/Апартаменты*')),
                ('old_new', models.CharField(choices=[(None, 'Выбрать'), ('Новостройка', 'Новостройка'), ('Вторичный рынок', 'Вторичный рынок')], max_length=20, verbose_name='Новостройка/Вторичный рынок*')),
                ('floor', models.CharField(max_length=2, verbose_name='Этаж*')),
                ('rooms_amount', models.CharField(max_length=8, verbose_name='Количество комнат*')),
                ('living_space', models.FloatField(blank=True, null=True, verbose_name='Жилая площадь')),
                ('kitchen_area', models.FloatField(blank=True, null=True, verbose_name='Площадь кухни')),
                ('ceiling_height', models.FloatField(blank=True, null=True, verbose_name='Высота потолков')),
                ('video_link', models.CharField(blank=True, max_length=20, null=True, verbose_name='Ссылка на видео')),
                ('repair', models.CharField(blank=True, max_length=20, null=True, verbose_name='Ремонт')),
                ('furniture', models.CharField(blank=True, max_length=20, null=True, verbose_name='Мебель')),
                ('building_type', models.CharField(blank=True, max_length=20, null=True, verbose_name='Тип дома')),
                ('max_floor', models.CharField(max_length=2, verbose_name='Количество этажей в доме*')),
                ('passenger_elevator', models.CharField(blank=True, max_length=20, null=True, verbose_name='Пассажирский лифт')),
                ('cargo_elevator', models.CharField(blank=True, max_length=20, null=True, verbose_name='Грузовой лифт')),
                ('yard', models.CharField(blank=True, max_length=20, null=True, verbose_name='Двор')),
                ('parking', models.CharField(blank=True, max_length=20, null=True, verbose_name='Парковка')),
                ('year', models.SmallIntegerField(blank=True, null=True, verbose_name='Год постройки')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bboard.action', verbose_name='Действие')),
                ('item_type', models.ForeignKey(default='apartment', editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='apartment', to='bboard.type', verbose_name='Тип объекта*')),
            ],
            options={
                'verbose_name': 'Квартира/Апартаменты',
                'verbose_name_plural': 'Квартиры/Апартаменты',
                'ordering': ['-time_update'],
            },
        ),
    ]