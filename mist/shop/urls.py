from django.urls import path
from . import views
from .views import ProductListView, ProductDetailView

app_name = "shop"
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', ProductListView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]
