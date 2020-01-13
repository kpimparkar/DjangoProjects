from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def create_user(request):
    # return HttpResponse("User creation page")

    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        # Using custom form UserRegisterForm as it has additional email field
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, f"User creation successful: "
                                      f"{form.cleaned_data.get('username')}")
            form.save()
            return redirect('blog-home')
        else:
            messages.error(request, "Form invalid")
    elif request.method == "GET":
        # form = UserCreationForm()
        form = UserRegisterForm()
    else:
        # form = UserCreationForm()
        form = UserRegisterForm()

    return render(request, 'users/user_register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
