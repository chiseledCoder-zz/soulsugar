from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

BLOG_CATEGORY = (
		("New Arrivals","New Arrivals"),
		("Healthy Treats","Healthy Treats"),
		("Cake","Cake"),
		("Recipe","Recipe"),
		("General","General"),
		("Diet","Diet"),
	)


class BlogCategory(models.Model):
	title = models.CharField(max_length=150)
	description = RichTextField()

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("post:details", kwargs={"title": self.title})

class PostQuerySet(models.query.QuerySet):
	def not_draft(self):
		return self.filter(draft=False)
	
	def published(self):
		return self.filter(publish=True).not_draft()

class PostManager(models.Manager):
	def get_queryset(self, *args, **kwargs):
		return PostQuerySet(self.model, using=self._db)
			
	def active(self, *args, **kwargs):
		# Post.objects.all() = super(PostManager, self).all()
		return self.get_queryset().published()

class Post(models.Model):
	user = models.ForeignKey(User, blank=True, null=True)
	title = models.CharField(max_length=120)
	image = models.ImageField(upload_to='post/images/', blank=True, null=True)
	category = models.ForeignKey('BlogCategory', blank=True, null=True)
	content = RichTextField()
	draft = models.BooleanField(default=True)
	publish = models.BooleanField(default=False)
	publish_date = models.DateField(default=timezone.now)
	slug = models.SlugField(unique=True)
	tags = models.ManyToManyField('Tag')
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	objects = PostManager()

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("post:details", kwargs={"slug": self.slug})

	class Meta:
		ordering = ["-timestamp", "-updated"]

	def save(self, *args, **kwargs):
		self.slug = "-".join((slugify(self.title), str(self.id)))
		return super(Post, self).save(*args, **kwargs)


class Tag(models.Model):
	title = models.CharField(max_length=150)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("post:details", kwargs={"title": self.title})
