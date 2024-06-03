from django.db import transaction
from django.db.models import F
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
# Create your views here.
from .serializers import *
from .models import *


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class CreateOrderAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer

    def create(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                items = self.request.data.pop('products')
                order = Order.objects.create(**self.request.data)
                total_price = 0
                for item in items:
                    try:
                        new_order_item = OrderProduct.objects.create(order=order, **item)
                        total_price += int(new_order_item.product.price) * new_order_item.quantity
                    except OrderProduct.DoesNotExist:
                        return Response(data={'error': 'Cart item does not exist'}, status=400)
                order.total_price = total_price
                order.save()
                return Response(data={'order_id': order.id}, status=201)
        except Exception as e:
            return Response(data={'error': str(e)}, status=500)




class CategoryListAPIView(ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()


class SubCategoryListAPIView(ListAPIView):
    serializer_class = SubCategoryListSerializer
    queryset = SubCategory.objects.all()


class ReviewAPIView(CreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class ContactAPIView(CreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contacts.objects.all()


class QuestionAPIView(CreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Questions.objects.all()
