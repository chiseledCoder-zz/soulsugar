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
	product_category = models.ForeignKey('ProductCategory', default="")
	price = models.DecimalField(max_digits=10, decimal_places=2)
	weight = models.CharField(max_length=50)
	image = models.ImageField(upload_to="products/", default="products/default.jpg")
	featured = models.BooleanField(default=False)
	slug = models.SlugField(unique=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["-timestamp"]

	def save(self, *args, **kwargs):
		self.slug = "-".join((slugify(self.product_category), (slugify(self.name)), str(self.id)))
		return super(Product, self).save(*args, **kwargs)
			

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


class Testimonial(models.Model):
	user_name = models.CharField(max_length=150)
	user_photo = models.ImageField(default="images/avatar/avatar_120x120.jpg")
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.user_name

	def __str__(self):
		return self.user_name

	class Meta:
		ordering = ["-timestamp"]
