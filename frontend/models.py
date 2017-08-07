from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import pre_save

# Create your models here.
class ProductCategory(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(null=True, blank=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(null=True, blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	weight = models.CharField(max_length=50)
	image = models.ImageField(upload_to="products/", default="products/default.jpg")
	slug = models.SlugField(unique=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Product.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Product)