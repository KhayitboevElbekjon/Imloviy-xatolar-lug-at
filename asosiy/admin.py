from django.contrib import admin
from .models import *
admin.register(Xato)

@admin.register(Togri)
class TogriAdmin(admin.ModelAdmin):
    list_display = ('soz',)


@admin.register(Xato)
class XatoAdmin(admin.ModelAdmin):
    list_display = ('notogri','stogri_fk')

