from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views import View
from django.urls import reverse_lazy

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
        return redirect(self.success_url)


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
        return redirect(self.success_url)


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect("shop:index")

# Temporary
def profile(request):
    return render(request, "users/profile.html")