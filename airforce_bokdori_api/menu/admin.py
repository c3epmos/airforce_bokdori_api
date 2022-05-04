from django.contrib import admin
from menu.models import Menu
from django.contrib import admin

class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'cycle', 'location', 'menu1', 'menu2', 'menu3', 'menu4', 'menu5']

admin.site.register(Menu, MenuAdmin)