from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views import View

class CreateUserView(FormView):
    template_name = "users/register_page.html"
    form_class = CreateUserForm

    def get(self, request):
        form = self.form_class()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account was created successful for {form.cleaned_data["username"]}')

            new_user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"]
            )
            login(request, new_user)
            return redirect('shop:index')

        context = {'form': form}
        return render(request, 'users/register_page.html', context)


class UserLoginView(FormView):
    template_name = "users/login_page.html"
    form_class = LoginUserForm

    def get(self, request):
        form = self.form_class()
        message = ""
        context = {
            "form": form,
            "message": message
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"]
            )
            if user is not None:
                login(request, user)
                return redirect("shop:index")

            else:
                messages.info(request, "Oops, thats not a match.")


        context = {
            "form": form,
        }

        return render(request, self.template_name, context)


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect("shop:index")

# Temporary
def profile(request):
    return render(request, "users/profile.html")