from django.urls import path

from . import views
from .views import ProductDetailView

urlpatterns = [
    path('', views.home, name='home'),
]
