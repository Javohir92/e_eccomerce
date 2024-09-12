from django.contrib import admin
from .models import Category, Product, ProductColor, ProductImage, ProductReview, ProductSize, Product, Wishlist
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductColor)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
admin.site.register(ProductSize)
admin.site.register(Wishlist)
