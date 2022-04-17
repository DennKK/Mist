from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView


def index(requests):
    return render(requests, 'shop/index.html')


class ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'shop/product_list.html'


class ProductDetailView(DetailView):
    model =  Product
    slug_field = 'url'
    template_name = 'shop/product_detail.html'
