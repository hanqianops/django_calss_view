# coding: utf-8
__author__ = "HanQian"
from django.contrib import admin
from .models import HostInfo

class HostAdmin(admin.ModelAdmin):
    list_display = ('hostname','ip','cpu','mem','deviceclass')


admin.site.register(HostInfo,HostAdmin)
