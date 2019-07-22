from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Order, Category, Product, Product_att, ListItem, STATUSES
from .serializers import OrderSerializer, CategorySerializer, ProductSerializer, Product_attSerializer, ListItemSerializer
 

# class ProductListAPIView(APIView):

#     def get(self, request):
#         products = Product.objects.all()
#         data = ProductSerializer(products, many=True).data
#         return Response(data=data)

# class ProductsAPIView(APIView):

#     def get(self, request, id, *args, **kwargs):
#         try:
#             product = Product.objects.get(id=id)
#         except ObjectDoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         data = ProductSerializer(product).data
#         return Response(data=data, status=status.HTTP_200_OK)
class ProductViewSet(viewsets.ModelViewSet):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
        queryset = Order.objects.all()
        serializer_class = OrderSerializer
