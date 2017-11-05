from django.conf import settings
from django.shortcuts import render
from .models import *
from django.core.mail import send_mail

# Create your views here.
def index_page(request):
	featured_products = Product.objects.filter(featured=True)[:7]
	new_products = Product.objects.all()[:10]
	product_category = ProductCategory.objects.all()
	testimonials = Testimonial.objects.all()[:5]
	template = 'index.html'
	context = {
		"site_name":"Home Page",
		"featured_products": featured_products,
		"new_products": new_products,
		"product_category": product_category,
		"testimonials": testimonials,
	}
	return render(request, template, context)

def about_us_page(request):
	template = "about.html",
	context = {
		"site_name": "About Us"
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

def contact_form(request):
	if request.method == "POST":
		contact_name = request.POST['contact_name']
		contact_email = request.POST['contact_email']
		contact_message = request.POST['contact_message']
		email_message = str(contact_message) + "\n by " + str(contact_name)+ "\n " + str(contact_email)

		send_mail("New inquiry from Soul Sugar Website", email_message, settings.EMAIL_HOST_USER, ['soulsugarbakery@gmail.com'], fail_silently=False)
		
	context = {
		"success" : "We have received your message. Will get back to you shortly!"
		"site_name": "Contact Submission"
	}
	return render(request, 'contact.html', context)