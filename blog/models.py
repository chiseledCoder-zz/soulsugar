from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.


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
	slug = models.SlugField(unique=True)
	image = models.ImageField(upload_to='post/images/')
	content = models.TextField()
	draft = models.BooleanField(default=False)
	publish = models.BooleanField(default=False)
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


def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Post.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)
