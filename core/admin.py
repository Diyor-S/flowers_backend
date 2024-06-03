from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ['id']
    search_fields = ['title']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category']
    list_filter = ['id']
    search_fields = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'special_offers', 'occasion', 'for_whom', 'status',
                    'quantity', 'price', 'old_price', 'sub_category']
    list_filter = ['status']
    search_fields = ['title']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'images', 'product']
    list_filter = ['product']


@admin.register(TogetherPurchased)
class TogetherPurchasedAdmin(admin.ModelAdmin):
    list_display = ['id', 'main_product', 'related_product']
    list_filter = ['id']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'review', 'created_at']
    list_filter = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone_number', 'status', 'address']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'payment', 'delivery', 'quantity']
    list_filter = ['order']


@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['phone_number1', 'phone_number2', 'email', 'address', 'work_time']
    list_filter = ['id']


@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone_number', 'question']
    list_filter = ['id']
