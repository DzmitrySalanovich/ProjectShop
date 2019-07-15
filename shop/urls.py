from django.urls import path
from shop import views

urlpatterns = [
    path('products/<id>/', views.ProductsAPIView.as_view(), name='product'),
    path('products/', views.ProductListAPIView.as_view(), name='products'),
    # path('shop/', views.product_list),
        # ('shop/', product_list_specific),
        # ('shop/', order_list),
        # ('shop/', order_spec_list),
        # ('shop/', order_create_list),
]