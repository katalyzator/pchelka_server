# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import smart_unicode

from main.models import Subcategory, Executer


class Application(models.Model):
    description = models.TextField(verbose_name=u'Описание', null=True)
    price = models.FloatField(default=1.0, max_length=255, verbose_name=u'Бюджет', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name=u'Адрес', null=True)
    number = models.CharField(max_length=255, verbose_name=u'Номер телефона', null=True)
    subcategory = models.ForeignKey(Subcategory, verbose_name=u'Категория', null=True, related_name='subcategories')
    active = models.BooleanField(verbose_name=u'Выполнено')
    executor = models.ForeignKey(Executer, verbose_name=u'Исполнитель', blank=True, null=True,
                                 related_name='application_executor')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=u'Дата создания')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.description)

    class Meta:
        verbose_name_plural = u'Заявки на сервис'
        verbose_name = u'Заявку'
        ordering = ['active', 'timestamp']

