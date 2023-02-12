from django.contrib import admin
from .models import Product,ReviewRating


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available', 'slug')


admin.site.register(Product, ProductAdmin)
admin.site.register(ReviewRating)