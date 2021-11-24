from django.contrib import admin

from core.models import *


class OpcionInline(admin.TabularInline):
    model = Opcion
    #fields = ['opcion']


class IpInline(admin.TabularInline):
    model = Ip


class EncuestaAdmin(admin.ModelAdmin):
    inlines = [OpcionInline, IpInline]


admin.site.register(Encuesta, EncuestaAdmin)
