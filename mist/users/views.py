from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, LoginUserForm, EditProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.generic import View, TemplateView
from django.urls import reverse_lazy
from .models import Profile
from django.contrib.auth.models import User


class CreateUserView(FormView):
    template_name = "users/register_page.html"
    form_class = CreateUserForm
    success_url = reverse_lazy("shop:index")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, f'Account was created successful for {form.cleaned_data["username"]}')

        new_user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"]
        )

        login(self.request, new_user)
        return super().form_valid(form)


class UserLoginView(FormView):
    template_name = "users/login_page.html"
    form_class = LoginUserForm
    success_url = reverse_lazy("shop:index")

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"]
        )

        login(self.request, user)
        return super().form_valid(form)


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect("shop:index")


class UserProfileView(View):
    def get(self, request):
        form = EditProfileForm(instance=request.user.profile)
        contex = {"form": form}
        return render(request, "users/profile.html", contex)

    def post(self, request):
        form = EditProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile,
        )
        if form.is_valid():
            form.save()
            return redirect("users:profile")
