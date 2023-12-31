from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
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


def CustomerDetails(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record.objects.get(id=pk)
		return render(request, 'CRMapp/record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

def DeleteRecord(request, pk):
	if request.user.is_authenticated:
		user = Record.objects.get(id=pk)
		user.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "please Log in...")
		return redirect('home')

def AddCustomer(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Customer Record Added...")
				return redirect('home')
		return render(request, 'CRMapp/addcustomer.html', {'form':form})
	else:
		messages.success(request, "Please Log In...")
		return redirect('home')

def UpdateCustomerDetails(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Details Has Been Updated!")
			return redirect('home')
		return render(request, 'CRMapp/updatecustomer.html', {'form':form})
	else:
		messages.success(request, "Please Log in...")
		return redirect('home')