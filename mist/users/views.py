from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def register_page(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
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
    return render(request, 'shop/register_page.html', context)


def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Oops, thats not a match.')

    context = {}
    return render(request, 'shop/login_page.html', context)
