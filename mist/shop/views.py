from django.shortcuts import render
from .models import Product
from django.views.generic import ListView


def index(requests):
    return render(requests, 'shop/index.html')


class ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'