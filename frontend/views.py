from django.shortcuts import render

# Create your views here.
def index(request):
	template = 'index.html'
	context = {
		"site_name":"Soul Sugar"
	}
	return render(request, template, context)

def contact(request):
	template = "contact.html"
	context = {
		"site_name" : "Contact Us"
	}
	return render(request, template, context)