from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomerRegisterForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and not user.is_superuser:
            login(request, user)
            return redirect('book:home')
    return render(request, 'customer/login.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book:home')
    else:
        form = CustomerRegisterForm()
    return render(request, 'customer/register.html', {'form': form})