from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, UserProductRelationship
from django.views.generic import ListView, DetailView, TemplateView, View, FormView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView
from .forms import ReviewForm
from django.urls import reverse_lazy, reverse


class ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'shop/product_list.html'


class ProductDisplay(DetailView):
    model = Product
    slug_field = "url"
    template_name = "shop/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm()
        return context


class PostReview(SingleObjectMixin, FormView):
    model = Product
    form_class = ReviewForm
    template_name = 'shop/product_detail.html'


class ProductDetailView(View):
    def get(self, request, *args, **kwargs):
        view = ProductDisplay.as_view()
        return view(request, *args, **kwargs)



'''
# TEMPORARY
class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, url=slug)
        try:
            review = request.user.user_product_relationship.get(product=product)
            form = ReviewForm(
                instance=review
            )
        except:
            form = ReviewForm()

        context = {
            "product": product,
            "form": form,
        }
        return render(request, "shop/product_detail.html", context)

    def post(self, request, slug):
        #product = get_object_or_404(Product, url=slug)
        try:
            review = request.user.user_product_relationship.get(product=self.product)
            form = ReviewForm(
                request.POST,
                instance=review
            )
            if form.is_valid():
                form.save()
            return redirect("shop:products")
        except:
            form = ReviewForm(request.POST)
            if form.is_valid():
                new_review = form.save(commit=False)
                new_review.self.product = self.product
                new_review.user = request.user
                new_review.save()
                return redirect("shop:products")
'''

'''
class ProductDetailView(DetailView):
    model =  Product
    slug_field = 'url'
    template_name = 'shop/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['user_product_relations'] = UserProductRelationship.objects.all()
        return context
'''


class IndexView(TemplateView):
    template_name = 'shop/index.html'
