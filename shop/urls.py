from django.urls import path, include
from shop import views

urlpatterns = [
    path('shop/', views.product_list),
        ('shop/', product_list_specific),
        ('shop/', order_list),
        ('shop/', order_spec_list),
        ('shop/', order_create_list),
]