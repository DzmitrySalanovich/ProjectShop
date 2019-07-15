from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Order, Category, Product, Product_att, ListItem, STATUSES
from .serializers import OrderSerializer, CategorySerializer, ProductSerializer, Product_attSerializer, ListItemSerializer
 
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.filter(STATUSES='Available')
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    
def product_list_specific(request):
    if request.method == 'GET':
        products = Product.object.filter(products_att=Product_att.object.all())
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
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