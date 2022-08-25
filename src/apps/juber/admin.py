# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Model, Vehicle, Location, Driver, Trip


admin.site.site_header = 'WhereismyJojo Admin'
admin.site.site_title = 'WhereismyJojo Admin'

admin.site.register(Model)
admin.site.register(Vehicle)
admin.site.register(Location)
admin.site.register(Driver)
admin.site.register(Trip)

