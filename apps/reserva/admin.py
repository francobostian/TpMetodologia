# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Host)
admin.site.register(Reservation)
admin.site.register(City)


class Availability(admin.TabularInline):
    model = AvailableDay
    fk_name = 'property'
    extra = 0


class PropertyAdmin(admin.ModelAdmin):
    inlines = [Availability, ]


admin.site.register(Property, PropertyAdmin)
