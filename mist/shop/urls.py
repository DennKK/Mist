from django.urls import path
from . import views
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', ProductListView.as_view()),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('register/', views.register_page, name='register_page'),
    path('login/', views.login_page, name='login_page'),
]
