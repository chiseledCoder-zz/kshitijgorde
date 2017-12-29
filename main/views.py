# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import AboutMe
from project.models import Project
from blog.models import Post
# Create your views here.

def home(request):
	aboutme = AboutMe.objects.all()[:1]
	project_list = Project.objects.filter(enable=True)
	blog = Post.objects.active()[:5]
	template = "index.html"
	context = {
		"site_title": "Kshitij Gorde Website",
		"aboutme": aboutme,
		"project_objects": project_list,
	}
	return render(request, template, context)