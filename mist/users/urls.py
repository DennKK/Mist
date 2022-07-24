from django.urls import path
from . import views
from .views import UserLoginView, CreateUserView, UserLogoutView, UserProfileView


app_name = "users"

urlpatterns = [
    path('register/', CreateUserView.as_view(), name="register"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
    path('profile/', UserProfileView.as_view(), name="profile")
]