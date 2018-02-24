# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import smart_unicode


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Подкатегории'

    title = models.CharField(max_length=1000, verbose_name='Категория')

    image = models.ImageField(upload_to='images/category', verbose_name='Image', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.title)


class Subcategory(models.Model):
    class Meta:
        verbose_name = 'Подкатегорию'
        verbose_name_plural = 'Подкатегории'

    title = models.CharField(max_length=1000, verbose_name='Подкатегория')
    parent_category = models.ForeignKey(Category, verbose_name='Название категории')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.title)


class Executer(models.Model):
    class Meta:
        verbose_name = u"Исполнителя"
        verbose_name_plural = u"Исполнители Биржы"

    user = models.ForeignKey(User, verbose_name=u'Пользователь', related_name='executer_user')
    full_name = models.CharField(max_length=255, verbose_name=u'ФИО')
    profession = models.ManyToManyField(Subcategory, verbose_name=u'Выберите род деятельности',
                                        related_name='profession_user')
    active = models.BooleanField(default=False, verbose_name=u"Активный статус")
    balance = models.FloatField(default=0, verbose_name=u"Баланс исполнителя")

    def __unicode__(self):
        return smart_unicode(self.full_name)
