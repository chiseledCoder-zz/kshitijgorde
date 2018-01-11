# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
from django.contrib.sitemaps import ping_google
from django.core.validators import RegexValidator
# Create your models here.
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+999999999'. Up to 13 digits allowed.")
class AboutMe(models.Model):
	full_name = models.CharField(max_length=150)
	description = RichTextField()
	display_pic = models.ImageField(default="profile/default.png", upload_to='profile/')
	tagline = models.CharField(max_length=100, default="")
	dob = models.DateField('Date')
	age = models.IntegerField(default=24)
	address = models.TextField(default="")
	nationality = models.CharField(max_length=50, default="Indian")
	email = models.EmailField(default="")
	phone_number = models.CharField(validators=[phone_regex], blank=False,max_length=20, default="")
	job_position = models.CharField(max_length=250, default="")
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

SkillCategories = (
		("Professional Skills", "Professional Skills"),
		("Software Skills", "Software Skills"),
		("Additional Skills", "Additional Skills"),
		("Language Skills", "Language Skills"),
	)

class Skill(models.Model):
	category = models.CharField(max_length=100, choices=SkillCategories, default="Professional Skills")
	title = models.CharField(max_length=250)
	count = models.IntegerField()
	enable = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title


class Testimonial(models.Model):
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