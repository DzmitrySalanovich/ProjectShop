from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, Category, Product, Product_att, ListItem, STATUSES
from .serializers import OrderSerializer, CategorySerializer, ProductSerializer, Product_attSerializer, ListItemSerializer
 

class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        data = ProductSerializer(products, many=True).data
        return Response(data=data)

class ProductsAPIView(APIView):
#     authentication_classes = ()
#     permission_classes = ()

    def get(self, request, id, *args, **kwargs):
        try:
            product = Product.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        data = ProductSerializer(product).data
        return Response(data=data, status=status.HTTP_200_OK)


def product_list(request):
    if request.method == 'GET':
        products = Product.objects.filter(STATUSES='Available')
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    
def product_list_specific(request):
    if request.method == 'GET':
        products_att = Product_att.objects.filter(products=Product.object.all())
        serializer = ProductSerializer(products_att, many=True)
        return JsonResponse(serializer.data, safe=False)

def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.filter()
        serializer = OrderSerializer(orders, many=True)
        return JsonResponse(serializer.data, safe=False)

def order_spec_list(request):
    if request.method == 'GET':
        orders_spec = Order.get_objects(pk)
        serializer = OrderSerializer(orders_spec, many=True)
        return JsonResponse(serializer.data, safe=False)
    
def order_create_list(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)