from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=="POST":
        form= RegisterForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            form.save()
            messages.success(request,f"Welcome {username} , Your account is created")
            return redirect('food:index')
    else:
        form= RegisterForm()
    return render(request,'users/register.html',{"form":form})
 
