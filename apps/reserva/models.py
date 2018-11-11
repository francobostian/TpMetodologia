# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.conf import settings
# Create your models here.


class City(models.Model):
    description = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Cities'

    def __unicode__(self):
        return self.description


private_storage = FileSystemStorage(location=settings.PRIVATE_STORAGE_ROOT)


class Host(models.Model):
    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Property(models.Model):
    description = models.CharField(max_length=50)
    image_url = models.ImageField(upload_to="images")
    tariff = models.DecimalField(max_digits=8, decimal_places=2)
    host = models.ForeignKey(Host)
    city = models.ForeignKey(City)

    class Meta:
        verbose_name_plural = 'Properties'

    def __unicode__(self):
        return self.description


class Reservation(models.Model):
    property = models.ForeignKey(Property)
    date = models.DateTimeField(default=timezone.now())
    guest = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=8, decimal_places=2)

    def __unicode__(self):
        return str(self.date)


class AvailableDay(models.Model):
    date = models.DateTimeField()
    reservation = models.ForeignKey(Reservation, blank=True, null=True)
    property = models.ForeignKey(Property)

    def __unicode__(self):
        return str(self.date)