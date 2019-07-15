# Generated by Django 2.2.3 on 2019-07-15 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('SKU', models.IntegerField()),
                ('discount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('category', models.ManyToManyField(to='shop.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product_att',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('value', models.DecimalField(decimal_places=3, max_digits=10)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datatime', models.DateTimeField(auto_now_add=True)),
                ('cost', models.DecimalField(decimal_places=3, max_digits=10)),
                ('cc_number', models.CharField(max_length=15)),
                ('status', models.CharField(choices=[('in_progress', 'In progress'), ('available', 'Available'), ('paid', 'Paid')], max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_SKU', models.IntegerField()),
                ('datatime', models.DateTimeField(verbose_name='date ordered')),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
        ),
    ]
