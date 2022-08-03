from django.urls import path
from . import views
from .views import ProductListView, ProductDetailView

app_name = "shop"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('products/', ProductListView.as_view(), name="products"),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name="product_detail"),
]
