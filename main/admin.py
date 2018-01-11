# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.
class MyDistinguishingPointAdmin(admin.ModelAdmin):
	list_display = ("title", "enable")

class StatAdmin(admin.ModelAdmin):
	list_display = ("title", "count","category", "enable")

class TestimonialAdmin(admin.ModelAdmin):
	list_display = ("given_by_name", "designation", "enable")

admin.site.register(AboutMe)
admin.site.register(MyDistinguishingPoint, MyDistinguishingPointAdmin)
admin.site.register(Stat, StatAdmin)
admin.site.register(Testimonial, TestimonialAdmin)