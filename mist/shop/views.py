from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from . models import Product


def home(requests):
    return HttpResponse('Hello')


class ProductDetailView(DetailView):
    model = Product
    query_pk_and_slug = True