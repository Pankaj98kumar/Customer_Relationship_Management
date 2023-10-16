from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

def Home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #Authenticate
        user = authenticate(request, username=username ,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in succesfully...")
            return redirect('home')
        else:
            messages.success(request, "Username or password didn't match , please try again !")
            return redirect('home')
    else:
        return render(request,'CRMapp/home.html',{'records':records})

def Login(request):
    pass

def Logout(request):
    logout(request)
    messages.success(request, "You have been Logged Out!...")
    return redirect('home')

def Register(request):
    if request.method == 'POST' :
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password = password)
            login(request, user)
            messages.success(request, 'Successfully Register...')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'CRMapp/register.html',{'form':form})
    return render(request,'CRMapp/register.html',{'form':form})



