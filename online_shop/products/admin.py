from django.contrib import admin
from .models import Category, Product, Review, Favorite, CartItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    
admin.site.register(Review)
admin.site.register(Favorite)
admin.site.register(CartItem)