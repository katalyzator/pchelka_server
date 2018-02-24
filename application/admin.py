# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django.contrib.admin import DateFieldListFilter

from application.models import Application


# TODO realize notification system https://github.com/v1k45/django-notify-x
class ApplicationAdmin(admin.ModelAdmin):
    list_editable = ['active', ]
    list_display = ['description', 'price', 'active', 'address', 'number', 'executor']
    list_filter = ['executor', ('timestamp', DateFieldListFilter), 'price', 'active']

    search_fields = ['description', 'executor']


admin.site.register(Application, ApplicationAdmin)
