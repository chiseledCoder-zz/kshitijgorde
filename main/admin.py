# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.
class MyDistinguishingPointAdmin(admin.ModelAdmin):
	list_display = ("title", "enable")

class SkillAdmin(admin.ModelAdmin):
	list_display = ("title", "count","category", "enable")

class TestimonialAdmin(admin.ModelAdmin):
	list_display = ("given_by_name", "designation", "enable")

class EducationAdmin(admin.ModelAdmin):
	list_display = ("school_name", "degree", "currently_studying", "left")


class WorkExperienceAdmin(admin.ModelAdmin):
	list_display = ("employer", "designation", "currently_working", "left")



admin.site.register(AboutMe)
admin.site.register(MyDistinguishingPoint, MyDistinguishingPointAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)