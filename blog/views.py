# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
# Create your views here.

def post_list(request):
	queryset_list = Post.objects.active()
	template = "blog/post_list.html"
	context = {
		"site_name": "Post List",
		"object_list": queryset_list
	}
	return render(request, template, context)

def post_detail(request, post_slug):
	instance = Post.objects.get(slug=post_slug)
	template = "blog/post_detail.html"
	context = {
		"site_name": instance.title,
		"object": instance,
	}
	return render(request, template, context)