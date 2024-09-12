from django.contrib import admin
from .models import Branch, Card, CartItem, DeliveryTariff, Discount, Order
# Register your models here.

admin.site.register(Branch)
admin.site.register(Card)
admin.site.register(CartItem)
admin.site.register(DeliveryTariff)
admin.site.register(Discount)
admin.site.register(Order)
