from django.contrib import admin
from .models import Post, Tag, BlogCategory
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = [
        'title',
        'draft',
        'publish',
        'publish_date'
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(BlogCategory)