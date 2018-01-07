# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.contrib.sitemaps import ping_google
# Create your models here.

class PostCategory(models.Model):
	title = models.CharField(max_length=150)
	slug = models.SlugField(unique=True, max_length=255)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		return super(PostCategory, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse("category_search", kwargs={"category_slug": self.slug})


class PostQuerySet(models.query.QuerySet):
	def not_draft(self):
		return self.filter(draft=False)
	
	def published(self):
		return self.filter(publish=True).not_draft()

class PostManager(models.Manager):
	def get_queryset(self, *args, **kwargs):
		return PostQuerySet(self.model, using=self._db)
			
	def active(self, *args, **kwargs):
		return self.get_queryset().published()

class Post(models.Model):
	title = models.CharField(max_length=255)
	description = RichTextField()
	meta_description = models.TextField(null="", blank=True)
	category = models.ForeignKey('PostCategory', blank=True, null=True)
	featured_image = models.ImageField(upload_to='products/images/', null=True, blank=True)
	associated_images = models.ManyToManyField('PostImage', blank=True)
	date = models.DateField('Date')
	tags = models.ManyToManyField('Tag')
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	slug = models.SlugField(unique=True, max_length=255)
	draft = models.BooleanField(default=True)
	publish = models.BooleanField(default=False)
	objects = PostManager()

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-date']
		
	def get_absolute_url(self):
		return reverse('blog:post_detail', kwargs={"post_slug": self.slug})

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		try:
			ping_google()
		except Exception:
			pass
		return super(Post, self).save(*args, **kwargs)

class PostImage(models.Model):
	image = models.ImageField(upload_to='blog/images/', default="blog/images/default.jpg")

	def __unicode__(self):
		return self.image.file.name


class Tag(models.Model):
	title = models.CharField(max_length=150)
	slug = models.SlugField(unique=True, default="")

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		return super(Tag, self).save(*args, **kwargs)
			
	def get_absolute_url(self):
		return reverse("tag_search", kwargs={"tag_slug": self.slug})