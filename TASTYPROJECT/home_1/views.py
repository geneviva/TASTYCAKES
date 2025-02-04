from django.shortcuts import render,redirect
from django.http import  HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages
# Create your views here.

@login_required(login_url='login')#refuses anonymous personnel to access inner web page
def index(request):
    return render(request, 'home/index.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:    
        form = CreateUserForm()
    
        if request.method == 'POST':
           form = CreateUserForm(request.POST)
           if form.is_valid():
               form.save()
               user = form.cleaned_data.get('username')
               messages.success(request, 'Account was created for '+user)
               return redirect('login')

    context = {'form':form} 
    return render(request,'home/register.html',context)       

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:    
        if request.method == 'POST':
           username=request.POST.get('username')
           password=request.POST.get('password')
        
           user = authenticate(request, username=username, password=password)
           if user is not None:
               login(request, user)
               return redirect('index')
           else:
               messages.info(request, 'Username OR password is incorrect')
            
    context = {}
    return render(request, 'home/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')