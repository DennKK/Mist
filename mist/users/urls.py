from django.urls import path
from . import views
from .views import UserLoginView

urlpatterns = [
    path('register/', views.register_page, name='register_page'),
    path('login/', UserLoginView.as_view(), name='login_page'),
]