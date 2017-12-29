# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ProjectCategory, Project, ProjectImage
# Register your models here.

admin.site.register(ProjectCategory)
admin.site.register(Project)
admin.site.register(ProjectImage)
