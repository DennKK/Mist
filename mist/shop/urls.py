from django.urls import path
from . import views
from .views import ProductListView

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', ProductListView.as_view()),
]
