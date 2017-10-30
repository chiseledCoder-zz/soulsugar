from django.contrib import admin
from .models import ProductCategory, Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display = [
        'name',
        'price',
        'weight',
        'featured',
    ]
		
admin.site.register(ProductCategory)
admin.site.register(Product, ProductAdmin)