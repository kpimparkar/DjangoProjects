from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def create_user(request):
    # return HttpResponse("User creation page")
    print(request.method)
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Form is valid")
        else:
            messages.error(request, "Form invalid")
    elif request.method == "GET":
        form = UserCreationForm()
    else:
        form = UserCreationForm()

    return render(request, 'users/user_register.html', {'form': form})
