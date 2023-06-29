from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm

def login_user(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('Credenciales exitosas!'))
            return redirect('home')
        else:
            messages.success(request, ('Credenciales incorrectas, trata de nuevo'))
            return redirect('employees/login_register', {'page': page})
            

    return render(request, 'employees/login_register.html', {'page': page})

def logout_user(request):
    logout(request)
    messages.success(request, ('Acabas de salir!'))
    return redirect('home')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if user is not None:
                login(request, user)
                messages.success(request, ('Registro exitoso'))
                return redirect('home')

    context = {'form': form, 'page': page}
    return render(request, 'employees/login_register.html', context)
    
