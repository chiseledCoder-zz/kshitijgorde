# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import AboutMe
# Create your views here.

def home(request):
	aboutme = AboutMe.objects.all()[:1]
	template = "index.html"
	context = {
		"site_title": "Kshitij Gorde Website",
		"aboutme": aboutme
	}
	return render(request, template, context)