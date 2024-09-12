from django.shortcuts import render
from rest_framework.generics import ListAPIView

from products.models import Category, Product
from products.serializers import CategoryListSerializers, ProductListSerializer


class CategoryListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers
    pagination_class = None
    
    
class ProductsListApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer