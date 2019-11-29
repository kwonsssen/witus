from django.contrib import admin
from .models import Basket_Team, Basket_member, Basket_team_maching, Basket_Team_Comment, Basket_team_maching_sinchung

@admin.register(Basket_Team)
class Basket_placeAdmin(admin.ModelAdmin):
    list_display = ('pk','basket_team_name','manager','area_detail', 'date_time')

@admin.register(Basket_member)
class Basket_placeAdmin(admin.ModelAdmin):
    list_display = ('pk','basket_team_names','user_name')

@admin.register(Basket_team_maching)
class Basket_placeAdmin(admin.ModelAdmin):
    list_display = ('pk','team_1','team_2')

@admin.register(Basket_team_maching_sinchung)
class Basket_placeAdmin(admin.ModelAdmin):
    list_display = ('pk','team_1','team_2','success')
    
@admin.register(Basket_Team_Comment)
class Basket_placeAdmin(admin.ModelAdmin):
    list_display = ('pk','team_name','author', 'text')
# Register your models here.


