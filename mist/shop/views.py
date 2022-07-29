from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, UserProductRelationship
from django.views.generic import ListView, DetailView, TemplateView, View, FormView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView
from .forms import ReviewForm
from django.urls import reverse_lazy, reverse
from django.core.exceptions import ObjectDoesNotExist


class ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'shop/product_list.html'


class ProductDisplay(DetailView):
    model = Product
    context_object_name = "product"
    slug_field = "url"
    template_name = "shop/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            review = self.request.user.user_product_relationship.get(product=kwargs['object'])
            context["form"] = ReviewForm(instance=review)
        except ObjectDoesNotExist:
            context["form"] = ReviewForm()

        return context


class PostReview(SingleObjectMixin, FormView):
    model = Product
    form_class = ReviewForm
    slug_field = "url"
    template_name = 'shop/product_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            review = self.request.user.user_product_relationship.get(product=self.object)
            print(f'{self.object} HEY')
            form = ReviewForm(
                self.request.POST,
                instance=review
            )
        except ObjectDoesNotExist:
            form = form.save(commit=False)
            form.product = self.object
            form.user = self.request.user

        form.save()

        return super().form_valid(form)

    def get_success_url(self):
        product = self.get_object()
        return reverse('shop:product_detail', kwargs={'slug': product.url}) + '#review'


class ProductDetailView(View):
    def get(self, request, *args, **kwargs):
        view = ProductDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostReview.as_view()
        return view(request, *args, **kwargs)


class IndexView(TemplateView):
    template_name = 'shop/index.html'

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
