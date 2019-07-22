from django.db import models
from authentication.models import User

STATUSES = [
    ('in_progress', 'In progress'),
    ('available', 'Available'),
    ('paid', 'Paid')
]

class Order(models.Model):
    
    # datatime = models.DateTimeField(auto_now_add=True)
    cost = models.DecimalField(max_digits=10, decimal_places=3)
    cc_number = models.CharField(max_length=15)
    status = models.CharField(choices=STATUSES, max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=30)
    category_id = models.ForeignKey(to='self', on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=30)
    SKU = models.IntegerField()
    discount = models.DecimalField(max_digits=10, decimal_places=3)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    quantity = models.IntegerField()
    category = models.ManyToManyField(to=Category)


class ListItem(models.Model):
    product_SKU = models.IntegerField()
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    datatime = models.DateTimeField('date ordered')
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    quantity = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class Product_att(models.Model):
    name = models.CharField(max_length=30)
    value = models.DecimalField(max_digits=10, decimal_places=3)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name