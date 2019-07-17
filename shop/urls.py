from django.urls import path, include
from shop import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.OrderViewSet)
router.register(r'', views.ProductViewSet)

urlpatterns = [
    path('products/', include(router.urls)),
    path('orders/', include(router.urls)),
]
