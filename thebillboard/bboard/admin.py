from django.contrib import admin
from .models import Apartment, Room, LandPlot, Parking, Action, Type

class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'apartment_type', 'action', 'price', 'time_create')
    list_display_links = ('id', 'apartment_type',)
    search_fields = ('specification',)
   # list_filter = ('published')
    #prepopulated_fields = {'slug': ('id',)} #генерация слага ссылки по title статьи

class RoomAdmin(admin.ModelAdmin):
        list_display = ('id', 'item_type', 'action', 'price', 'time_create')
        list_display_links = ('id', 'item_type', 'action',)
        search_fields = ('specification',)

class ParkingAdmin(admin.ModelAdmin):
    list_display = ('id', 'parking_type', 'action', 'price', 'time_create')
    list_display_links = ('id', 'parking_type', 'action',)
    search_fields = ('specification',)

class LandPlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_type', 'action', 'price', 'time_create')
    list_display_links = ('id', 'item_type', 'action',)
    search_fields = ('specification',)


admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Parking, ParkingAdmin)
admin.site.register(LandPlot, LandPlotAdmin)
admin.site.register(Action)
admin.site.register(Type)

# Register your models here.
