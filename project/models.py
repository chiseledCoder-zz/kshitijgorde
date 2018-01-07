# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.contrib.sitemaps import ping_google
# Create your models here.

class ProjectCategory(models.Model):
	title = models.CharField(max_length=250)
	slug = models.SlugField(unique=True)

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		try:
			ping_google()
		except Exception:
			pass
		super(Project, self).save(*args, **kwargs)

class Project(models.Model):
	title = models.CharField(max_length=250)
	description = RichTextField()
	category = models.ForeignKey('ProjectCategory', blank=True, null=True)
	featured_image = models.ImageField(upload_to='projects/images/', default="projects/images/default.jpg")
	associated_images = models.ManyToManyField('ProjectImage', blank=True)
	date = models.DateField('Date')
	ongoing = models.BooleanField(default=False)
	enable = models.BooleanField(default=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	slug = models.SlugField(unique=True)
	
	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-date']

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		try:
			ping_google()
		except Exception:
			pass
		super(Project, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('main:project_detail', kwargs={"project_slug": self.slug})

class ProjectImage(models.Model):
	image = models.ImageField(upload_to='projects/images/', default="projects/images/default.jpg")
	def __unicode__(self):
		return self.image.file.name