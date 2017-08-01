try:
	from urllib import quote_plus
except:
	pass

try: 
	from urllib.parse import quote_plus
except:
	pass


from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm
from .models import Post

# Create your views here.

def post_create(request):
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		message.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form":form,
	}
	return render(request, "blog/post_form.html", context)

def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	if instance.publish > timezone.now().date() or instance.draft:
		raise Http404
	share_string = quote_plus(instance.content)

	context = {
		"title" : instance.title,
		"instance": instance,
		"share_string": share_string
	}
	template = "blog/post_detail.html"
	return render(request, template, context)

def blog_list(request):
	today = timezone.now().date()
	queryset_list = Post.objects.active()
	query = request.GET.get('q')
	if query:
		queryset_list = queryset_list.filter(Q(title__icontains==query)|Q(content__icontains==query)).distinct()
	paginator = Paginator(queryset_list, 8)
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		query = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset,
		"site_name": "Blog List",
		"page_request_var": page_request_var,
		"today": today
	}
	template = "blog/blog_list.html"
	return render(request, template, context)