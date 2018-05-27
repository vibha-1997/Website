# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from website.models import UserProfile,room_category_size,room_category,dimensions


admin.site.register(UserProfile)
admin.site.register(room_category)
admin.site.register(room_category_size)
admin.site.register(dimensions)

# Register your models here.
