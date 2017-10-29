from django.shortcuts import render
from .models import *
# Create your views here.
def index_page(request):
	featured_products = Product.objects.filter(featured=True)[:5]
	new_products = Product.objects.all()[:10]
	product_category = ProductCategory.objects.all()
	template = 'index.html'
	context = {
		"site_name":"Home Page",
		"featured_products": featured_products,
		"new_products": new_products,
		"product_category": product_category
	}
	return render(request, template, context)

def cakes_page(request):
	template = "cakes.html",
	context = {
		"site_name": "Cakes"
	}
	return render(request, template, context)

def cupcakes_page(request):
	template = "cupcakes.html"
	context = {
		"site_name": "Cup Cakes",
	}
	return render(request, template, context)

def desserts_page(request):
	template = "desserts.html",
	context = {
		"site_name": "Desserts"
	}
	return render(request, template, context)

def healthy_treats_page(request):
	template = "healthy_treats.html"
	context = {
		"site_name": "Healthy Treats"
	}
	return render(request, template, context)

def corporates_page(request):
	template = "corporates.html"
	context = {
		"site_name": "Corporates",
	}
	return render(request, template, context)

def occasions_page(request):
	template = "occasions.html"
	context = {
		"site_name": "Occasions"
	}
	return render(request, template, context)

def contact_page(request):
	template = "contact.html"
	context = {
		"site_name" : "Contact Us",
	}
	return render(request, template, context)

