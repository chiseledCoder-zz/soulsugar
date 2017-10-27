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
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.utils import timezone
from .forms import PostForm
from .models import Post, Tag, BlogCategory

# Create your views here.

def post_detail(request, post_slug):
	instance = get_object_or_404(Post, slug=post_slug)
	if instance.draft == True:
		raise Http404
	share_string = quote_plus(instance.content)
	tags = Tag.objects.all()
	blog_categorys = BlogCategory.objects.all()
	recent_blogs_list = Post.objects.all()[:5]
	share_string = quote_plus(instance.content)
	context = {
		"site_name": "Blog - " + str(instance.title),
		"object": instance,
		"share_string": share_string,
		"tags": tags,
		"blog_categorys": blog_categorys,
		"recent_post_list": recent_blogs_list	
	}
	template = "blog/blog_detail.html"
	return render(request, template, context)

def blog_list(request):
	today = timezone.now().date()
	queryset_list = Post.objects.active()
	query = request.GET.get('q')
	if query:
		queryset_list = queryset_list.filter(Q(title__icontains==query)|Q(content__icontains==query)).distinct()
	paginator = Paginator(queryset_list, 10)
	page = request.GET.get("page")
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		query = paginator.page(paginator.num_pages)
	tags = Tag.objects.all()
	blog_categorys = BlogCategory.objects.all()
	recent_blogs_list = Post.objects.all()[:5]
	context = {
		"object_list": queryset,
		"site_name": "Blog List",
		"today": today,
		"tags": tags,
		"blog_categorys": blog_categorys,
		"recent_post_list": recent_blogs_list
	}
	template = "blog/blog_list.html"
	return render(request, template, context)


def tag_search(request, tag_slug):
	blogs = get_list_or_404(Post, tags__slug__iexact=tag_slug)
	tags = Tag.objects.all()
	blog_categorys = BlogCategory.objects.all()
	recent_blogs_list = Post.objects.all()[:5]
	template = "blog/blog_list.html"
	context = {
		"site_name": "Blog Search by "+ str(tag_slug),
		"tags": tags,
		"blog_categorys": blog_categorys,
		"object_list": blogs,
		"recent_post_list": recent_blogs_list
	}
	return render(request, template, context)

def category_search(request, category_slug):
	blogs = get_list_or_404(Post, category__slug__iexact=category_slug)
	tags = Tag.objects.all()
	blog_categorys = BlogCategory.objects.all()
	recent_blogs_list = Post.objects.all()[:5]
	template = "blog/blog_list.html"
	context = {
		"site_name": "Blog Search by "+ str(category_slug),
		"tags": tags,
		"blog_categorys": blog_categorys,
		"object_list": blogs,
		"recent_post_list": recent_blogs_list
	}
	return render(request, template, context)