from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, UserProductRelationship
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView
from .forms import ReviewForm
from django.urls import reverse_lazy


class ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'shop/product_list.html'


class ProductDetailView(DetailView):
    model =  Product
    slug_field = 'url'
    template_name = 'shop/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['user_product_relations'] = UserProductRelationship.objects.all()
        return context

class IndexView(TemplateView):
    template_name = 'shop/index.html'

