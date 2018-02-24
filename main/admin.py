# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from main.models import Category, Subcategory, Executer

admin.site.site_header = u"Панель управления биржой сервисных услуг ПЧЕЛКА"


class ExecutorAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'active', 'balance', 'professions']
    list_filter = ['profession', 'active', 'balance', 'full_name']
    search_fields = ['full_name']

    def professions(self, obj):
        return ",\n".join([p.title for p in obj.profession.all()])


admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Executer, ExecutorAdmin)
