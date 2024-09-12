from django.urls import path
from products.views import CategoryListApiView, ProductsListApiView


urlpatterns = [
    path('categories/', CategoryListApiView.as_view(), name='categories'),
    path('products/', ProductsListApiView.as_view(), name='products'),
]
