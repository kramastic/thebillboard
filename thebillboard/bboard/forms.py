from django.forms import ModelForm, Form
from .models import *
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='login')  # , widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='email')  # , widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='password')  # , widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='password2')  # , widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='login')  # , widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='password')  # w, widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class UserModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name_adv


class ActionChooseForm(forms.ModelForm):
    action = UserModelChoiceField(queryset=Action.objects.all(), empty_label='Выбрать', label='Продать/Сдать в аренду*')


class ValidateFloor():
    def clean_max_floor(self):
        value = self.cleaned_data['max_floor']
        if value < self.cleaned_data['floor']:
            raise ValidationError('Укажите правильное значение этажа расположения вашей недвижимости и максимального '
                                  'количества этажей в здании.')
        return value


class CatActForm(Form):
    item_type = UserModelChoiceField(queryset=Type.objects.all(), empty_label='Выбрать', label='Что у вас есть?')
    action = UserModelChoiceField(queryset=Action.objects.all(), empty_label='Выбрать', label='Что хотите сделать?')


class ApartmentForm(ActionChooseForm, ValidateFloor):
    class Meta:
        model = Apartment
        fields = (
        'action', 'apartment_type', 'old_new', 'address', 'total_area', 'rooms_amount', 'floor', 'living_space',
        'kitchen_area', 'ceiling_height', 'video_link', 'building_type', 'max_floor', 'passenger_elevator',
        'cargo_elevator', 'parking', 'specification', 'image', 'online_show', 'price', 'transaction_terms')

    def clean_max_floor(self):  # этаж квартиры не больше, чем этажей в здании
        value = self.cleaned_data['max_floor']
        if value < self.cleaned_data['floor']:
            raise ValidationError('Укажите правильное значение этажа расположения вашей недвижимости и максимального '
                                  'количества этажей в здании.')
        return value

    apartment_type = forms.ChoiceField(choices=apartment_type_list, label='Квартира/Апартаменты*')
    old_new = forms.ChoiceField(choices=old_new_list, label='Новостройка/Вторичный рынок*')
    parking = forms.MultipleChoiceField(choices=parking_adv_list, label='Парковка', widget=forms.CheckboxSelectMultiple)
    total_area = forms.FloatField(label='Общая площадь', label_suffix=', m2')
    online_show = forms.ChoiceField(choices=online_show_list, label='Онлайн показ')


class RoomForm(ActionChooseForm, ValidateFloor):
    class Meta:
        model = Room
        fields = ('action', 'room_in_total', 'address', 'total_area', 'floor',
                  'video_link', 'building_type', 'max_floor', 'specification', 'image', 'online_show', 'price',
                  'transaction_terms')

    total_area = forms.FloatField(label='Общая площадь', label_suffix=', m2')


class ParkingForm(ActionChooseForm, ValidateFloor):
    class Meta:
        model = Parking
        fields = ('action', 'parking_type', 'address', 'total_area',
                  'video_link', 'specification', 'image', 'online_show', 'price',
                  'transaction_terms')

    total_area = forms.FloatField(label='Общая площадь', label_suffix=', m2')


class LandPlotForm(ActionChooseForm, ValidateFloor):
    class Meta:
        model = LandPlot
        fields = ('action', 'address', 'total_area',
                  'video_link', 'specification', 'image', 'price',
                  'transaction_terms')

    total_area = forms.FloatField(label='Общая площадь', label_suffix=', m2')
