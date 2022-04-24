from django.urls import path
from . import views
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', ProductListView.as_view()),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_request, name='login_request'),
]
