from django.contrib import admin

from menu_app.models import Menu, MenuItem

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    pass


