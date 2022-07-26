from django.urls import path
from .views import CreateUserView, UserLogoutView, UserLoginView, UserProfileView, EditProfileView

app_name = "users"

urlpatterns = [
    path('register/', CreateUserView.as_view(), name="register"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
    path('profile/', UserProfileView.as_view(), name="profile"),
    path('profile/edit/', EditProfileView.as_view(), name="edit_profile")
]