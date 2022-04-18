from django.shortcuts import render, redirect
from .models import Product
from django.views.generic import ListView, DetailView
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            return redirect('index')
    else:
        form = SignUpForm()
    context = {'form': form, }
    return render(request, 'shop/signup.html', context)


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
    else:
        form = AuthenticationForm()
    context = {'form': form}

    return render(request, 'shop/login.html', context)