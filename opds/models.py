# -*- coding: utf-8 -*-
from django.db import models


class Char(models.Model):
    """ Буква, необходима для вывода в опдс """
    char = models.CharField(u"Буква", max_length=3)


class MenuItem(models.Model):
    title = models.CharField(u"Заголовок", max_length=300, null=True, blank=True)
    link = models.CharField(u"Ссылка", max_length=400, null=True, blank=True)
    description = models.TextField(u"Описание", null=True, blank=True)
    group = models.CharField(u"Группа", max_length=40, null=True, blank=True)
    order = models.IntegerField(u"Порядок", default=0)