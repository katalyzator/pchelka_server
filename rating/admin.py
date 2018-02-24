# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from rating.models import Rating

admin.site.register(Rating)
