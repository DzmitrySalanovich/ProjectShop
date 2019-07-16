from django.urls import path
from shop import views

urlpatterns = [
    path('products/<id>/', views.ProductsAPIView.as_view(), name='product'),
    path('products/', views.ProductListAPIView.as_view(), name='products'),
    path('product_list/', views.ShopAPIView.as_view(), name='products_list'),
    path('product_list_specific/', views.ShopAPIView.as_view(), name='product_list_specific'),
    path('order_list/', views.ShopAPIView.as_view(), name='order_list'),
    path('order_spec_list/<id>/', views.ShopAPIView.as_view(), name='order_spec_list'),
    path('order_create_list/', views.ShopAPIView.as_view(), name='order_create_list'),
]