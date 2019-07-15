from rest_framework import serializers
from .models import Order, Category, Product, Product_att, ListItem, STATUSES


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'datetime', 'cost', 'cc_number', 'status')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'category_id')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'SKU', 'discount', 'price', 'quantity', 'category')


class ListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListItem
        fields = ('id', 'product_SKU', 'order_id', 'datatime', 'name', 'price', 'quantity', 'product_id')


class Product_attSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_att
        fields = ('id', 'name', 'product_id')

