# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
from django.contrib.sitemaps import ping_google
# Create your models here.

class AboutMe(models.Model):
	full_name = models.CharField(max_length=150)
	description = RichTextField()
	display_pic = models.ImageField(default="profile/default.png", upload_to='profile/')
	tagline = models.CharField(max_length=100, default="")
	dob = models.DateField('Date')
	address = models.TextField(default="")
	nationality = models.CharField(max_length=50, default="Indian")
	email = models.EmailField(default="")
	phone = models.IntegerField(default="91 9096081092")
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	def __unicode__(self):
		return self.full_name

	def __str__(self):
		return self.full_name

class MyDistinguishingPoint(models.Model):
	title = models.CharField(max_length=250)
	description = RichTextField()
	enable = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

class Stats(models.Model):
	title = models.CharField(max_length=250)
	count = models.IntegerField()
	enable = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title


class Testimonials(models.Model):
	given_by_name = models.CharField(max_length=250)
	testimony = models.TextField()
	designation = RichTextField(max_length=250)
	enable = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.given_by_name

	def __str__(self):
		return self.given_by_name