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
from .models import Post, Tag, BlogCategory

# Create your views here.

def post_detail(request, slug):
	instance = get_object_or_404(Post, slug=slug)
	if instance.draft == True:
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
	tags = Tag.objects.all()
	blog_categorys = BlogCategory.objects.all()
	context = {
		"object_list": queryset,
		"site_name": "Blog List",
		"page_request_var": page_request_var,
		"today": today,
		"tags": tags,
		"blog_categorys": blog_categorys
	}
	template = "blog/blog_list.html"
	return render(request, template, context)


def tag_search(request, tag_name):
	blogs = Blog.objects.filter(tag__title__iexact=tag_name)
	tags = Tag.objects.all()
	blog_categorys = BlogCategory.objects.all()
	template = "blog/blog_list.html"
	context = {
		"site_name": "Blog Search by "+ str(tag_name),		
		"tags": tags,
		"blog_categorys": blog_categorys
	}
	return render(request, template, context)

def category_search(request, category_name):
	blogs = Blog.objects.filter(category=category_name)
	tags = Tag.objects.all()
	blog_categorys = BlogCategory.objects.all()
	all_tags = Tag.objects.all()
	template = "blog/blog_list.html"
	context = {
		"site_name": "Blog Search by "+ str(category_name),
		"tags": tags,
		"blog_categorys": blog_categorys
	}
	return render(request, template, context)