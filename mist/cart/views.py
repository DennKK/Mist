from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from .forms import CartAddProductForm
from shop.models import Product
from django.views.decorators.http import require_POST


@require_POST
def cart_add(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, url=slug)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd["quantity"],
            update_quantity=cd["update"]
        )
        return redirect("cart:cart_detail")


def cart_remove(request, slug):
    product = get_object_or_404(Product, ulr=slug)
    cart = Cart(request.POST)
    cart.remove(product)
    return redirect("cart:cart_detail")


def cart_detail(request):
    cart = Cart(request)
    return render(request, "cart/cart_detail.html", context={"cart": cart})
