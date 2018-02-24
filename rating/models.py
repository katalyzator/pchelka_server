# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.encoding import smart_unicode


class Rating(models.Model):
    class Meta:
        verbose_name_plural = u'Рейтинг специалистов'
        verbose_name = u'рейтинг'

    rating_range = models.FloatField(default=0.0, verbose_name='Выберите диапазон')
    user = models.ForeignKey(User, verbose_name='Пользователь')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.user)
