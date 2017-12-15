# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class AboutMe(models.Model):
	full_name = models.CharField(max_length=150)
	description = models.TextField()
	display_pic = models.ImageField(default="profile/default.png", upload_to='profile/')
	tagline = models.CharField(max_length=100, default="")
	dob = models.DateField('Date')
	address = models.TextField(default="")
	nationality = models.CharField(max_length=50, default="Indian")
	email = models.EmailField(default="")
	phone = models.IntegerField(default="91 9096081092")

	def __unicode__(self):
		return self.full_name

	def __str__(self):
		return self.full_name
