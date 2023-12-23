from django.contrib.auth.models import User
from django.db import models
from .utils import *
from django.forms import ModelChoiceField


class MainInfo(models.Model):
    class Meta:
        abstract = True

    action = models.ForeignKey('Action', null=False, blank=False, on_delete=models.PROTECT, verbose_name='Действие')
    address = models.CharField(max_length=100, verbose_name='Адрес*', null=False)
    specification = models.TextField(verbose_name='Описание*', null=False)
    total_area = models.FloatField(verbose_name='Общая площадь*', null=False)
    image = models.ImageField(verbose_name='Фотографии', null=True, blank=True)
    online_show = models.CharField(max_length=3, choices=online_show_list, verbose_name='Онлайн показ', null=True,
                                   blank=True)
    price = models.IntegerField(verbose_name='Цена*', null=False)
    transaction_terms = models.CharField(max_length=100, verbose_name='Условия сделки', null=True, blank=True)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.PROTECT,
                             editable=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)


class Action(models.Model):
    name = models.CharField(max_length=200, verbose_name='Действие', primary_key=True)
    name_adv = models.CharField(max_length=200)
    name_catalog = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Действия'
        verbose_name = 'Действие'
        ordering = ['name']

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=30, verbose_name='Тип недвижимости', primary_key=True)
    name_adv = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = 'Типы недвижимости'
        verbose_name = 'Тип недвижимости'
        ordering = ['name']

    def __str__(self):
        return self.name


class Apartment(MainInfo):
    class Meta:
        verbose_name_plural = 'Квартиры/Апартаменты'
        verbose_name = 'Квартира/Апартаменты'
        ordering = ['-time_update']

    def __str__(self):
        return f'apartment_type №{self.id}'

    item_type = models.ForeignKey('Type', default='apartment', on_delete=models.PROTECT, verbose_name='Тип объекта*',
                                  null=False, editable=False, related_name='apartment')
    apartment_type = models.CharField(max_length=11, choices=apartment_type_list, verbose_name='Квартира/Апартаменты*',
                                      null=False)
    old_new = models.CharField(max_length=15, choices=old_new_list, verbose_name='Новостройка/Вторичный рынок*',
                               null=False)
    floor = models.SmallIntegerField(verbose_name='Этаж*', null=False)
    rooms_amount = models.PositiveSmallIntegerField(verbose_name='Количество комнат*', choices=rooms_amount1,
                                                    null=False)
    living_space = models.FloatField(verbose_name='Жилая площадь', null=True, blank=True)
    kitchen_area = models.FloatField(verbose_name='Площадь кухни', null=True, blank=True)
    ceiling_height = models.FloatField(verbose_name='Высота потолков', null=True, blank=True)
    video_link = models.CharField(max_length=200, verbose_name='Ссылка на видео', null=True, blank=True)
    building_type = models.CharField(max_length=30, verbose_name='Тип дома', choices=building_type_list,
                                     null=True, blank=True)
    max_floor = models.PositiveSmallIntegerField(verbose_name='Количество этажей в доме*', null=False)
    passenger_elevator = models.PositiveSmallIntegerField(choices=lift_amount, verbose_name='Пассажирский лифт',
                                                          null=True, blank=True)
    cargo_elevator = models.PositiveSmallIntegerField(choices=lift_amount, verbose_name='Грузовой лифт', null=True,
                                                      blank=True)
    parking = models.CharField(max_length=100, verbose_name='Парковка', null=True, blank=True)
    year = models.PositiveSmallIntegerField(verbose_name='Год постройки', null=True, blank=True)


class Room(MainInfo):
    class Meta:
        verbose_name_plural = 'Комнаты'
        verbose_name = 'Комната'
        ordering = ['-time_update']

    def __str__(self):
        return f'Комната №{self.id}'

    item_type = models.ForeignKey('Type', default='room', on_delete=models.PROTECT, verbose_name='Тип объекта*',
                                  null=False, editable=False, related_name='room')
    room_in_total = models.SmallIntegerField(verbose_name='Всего комнат в квартире*', null=False)
    building_type = models.CharField(max_length=30, verbose_name='Тип дома', choices=building_type_list,
                                     null=True, blank=True)
    floor = models.SmallIntegerField(verbose_name='Этаж*', null=False)
    max_floor = models.SmallIntegerField(verbose_name='Количество этажей в доме*', null=False)
    video_link = models.CharField(max_length=200, verbose_name='Ссылка на видео', null=True, blank=True)


class Parking(MainInfo):
    class Meta:
        verbose_name_plural = 'Гаражи/Машиноместа'
        verbose_name = 'Гараж/Машиноместо'
        ordering = ['time_update']

    item_type = models.ForeignKey('Type', default='parking', on_delete=models.PROTECT, verbose_name='Тип объекта',
                                  null=False, editable=False, related_name='parking')
    parking_type = models.CharField(max_length=200, choices=parking_type_list, verbose_name='Гараж/Машиноместо*',
                                    null=False)
    video_link = models.CharField(max_length=200, verbose_name='Ссылка на видео', null=True, blank=True)


class LandPlot(MainInfo):
    class Meta:
        verbose_name_plural = 'Земельные участки'
        verbose_name = 'Земельный участок'
        ordering = ['-time_update']

    item_type = models.ForeignKey('Type', default='land_plot', on_delete=models.PROTECT, verbose_name='Тип объекта*',
                                  null=False, editable=False, related_name='land_plot')
    online_show = None
    video_link = models.CharField(max_length=200, verbose_name='Ссылка на видео', null=True, blank=True)
