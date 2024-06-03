from rest_framework import serializers
from common.serializers import MediaURLSerializer
from .models import *


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')
        read_only_fields = fields


class SubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id', 'title', 'category')
        read_only_fields = fields


class ProductListSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = Product
        fields = ('title', 'image', 'special_offers', 'price')
        read_only_fields = fields


class ProductImageSerializer(serializers.Serializer):
    image = MediaURLSerializer()


class TogetherPurchasedSerializer(serializers.ModelSerializer):
    related_products = ProductListSerializer()

    class Meta:
        model = TogetherPurchased
        fields = ('related_products',)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('review', 'product')
        read_only_fields = ('created_at',)


class ProductDetailSerializer(serializers.ModelSerializer):
    sub_category = SubCategoryListSerializer()
    image = MediaURLSerializer()
    product_images = ProductImageSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    related_products = TogetherPurchasedSerializer(many=True)

    class Meta:
        model = Product
        fields = ['related_products', 'image', 'product_images', 'reviews', 'title', 'special_offers', 'occasion',
                  'for_whom', 'description', 'status', 'quantity', 'price', 'sub_category']

        read_only_fields = ['related_products', 'image', 'product_images', 'reviews',
                            'title', 'special_offers', 'occasion',
                            'for_whom', 'description', 'status', 'quantity', 'price', 'sub_category']


class OrderProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class CreateOrderSerializer(serializers.ModelSerializer):
    products = serializers.ListField(child=OrderProductSerializer())

    class Meta:
        model = Order
        fields = ('name', 'phone_number', 'address', 'products')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ('phone_number1', 'phone_number2', 'email', 'address', 'work_time')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ('name', 'phone_number', 'question')

