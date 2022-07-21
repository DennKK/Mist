from django.urls import path
from . import views
from .views import UserLoginView, CreateUserView

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='register_page'),
    path('login/', UserLoginView.as_view(), name='login_page'),
]