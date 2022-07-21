from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, LoginUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.edit import FormView


class CreateUserView(FormView):
    template_name = "users/register_page.html"
    form_class = CreateUserForm

    def get(self, request):
        form = self.form_class()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        #if request.method == 'POST':
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account was created successful for {user}')

            new_user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"]
            )
            login(request, new_user)
            return redirect('index')

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
                return redirect("index")

            else:
                messages.info(request, 'Oops, thats not a match.')

        context = {
            "form": form,
        }

        return render(request, self.template_name, context)
