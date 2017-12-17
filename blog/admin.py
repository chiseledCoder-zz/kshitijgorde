# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.
def make_post_active(modeladmin, request, queryset):
	queryset.update(publish=True, draft=False)
	make_post_active.short_description = "Publish selected posts"


def make_post_inactive(modeladmin, request, queryset):
	queryset.update(publish=False, draft=True)
	make_post_inactive.short_description = "Draft selected posts"

class PostAdmin(admin.ModelAdmin):
	list_display = ("title", "category", "date", "draft", "publish")
	actions = [make_post_inactive, make_post_active]


admin.site.register(PostCategory)
admin.site.register(Post, PostAdmin)
admin.site.register(PostImage)
admin.site.register(Tag)