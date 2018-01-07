# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import *
from project.models import Project
from blog.models import Post
# Create your views here.

def home(request):
	aboutme = AboutMe.objects.all()[:1]
	distinguishing_points = MyDistinguishingPoint.objects.filter(enable=True)[:3]
	stats = Stats.objects.filter(enable=True)[:3]
	project_list = Project.objects.filter(enable=True)
	testimonial_list = models.objects.filter(enable=True)
	post_list = Post.objects.active()[:5]
	template = "index.html"
	context = {
		"site_title": "Kshitij Gorde Website",
		"aboutme_objects": aboutme,
		"distinguishing_points_objects": distinguishing_points,
		"stat_objects": stats,
		"project_objects": project_list,
		"testimonial_objects": testimonial_list,
		"blog_objects": post_list,
	}
	return render(request, template, context)