from django.contrib import admin
from .models import Basket_place, Place_Comment, Soccer_place, Foot_place

@admin.register(Basket_place)
class Basket_placeAdmin(admin.ModelAdmin):
    list_display = ('title','address','score')

@admin.register(Soccer_place)
class Basket_placeAdmin(admin.ModelAdmin):
    list_display = ('title','address','score')

@admin.register(Foot_place)
class Basket_placeAdmin(admin.ModelAdmin):
    list_display = ('title','address','score')

@admin.register(Place_Comment)
class Basket_placeAdmin(admin.ModelAdmin):
    list_display = ('place','author','text')

    