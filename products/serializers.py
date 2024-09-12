from rest_framework import serializers
from common.serializers import MediaSerializers
from .models import Category, Product


class CategoryListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ('image', )


class ProductListSerializer(serializers.ModelSerializer):
    thumbnail = MediaSerializers(read_only=True)
    
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'category', 'in_stock', 'brand', 'discount', 'thumbnail')