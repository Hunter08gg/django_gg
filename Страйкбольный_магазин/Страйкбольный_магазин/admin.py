from django.contrib import admin
from Страйкбольный_магазин.Страйкбольный_магазин.models import Weapon, Creater
# Register your models here.

#@admin.register(Weapon)
#lass PostAdmin(admin.ModelAdmin):
#    list_display = ["title", "created_at"]
admin.site.register(Weapon)
admin.site.register(Creater)
