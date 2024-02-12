from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def Login_Staff(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect based on user role
            if user.is_superuser:
                return redirect('admin_dashboard')
            elif user.role == 'Admin':
                return redirect('admin_dashboard')
            else:
                return redirect('admin_dashboard')  # Redirect others to a default dashboard
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid login credentials'})

    return render(request, 'login.html')

def Logout_Staff(request):
    logout(request)
    return redirect('Login_Staff')

def signup(request):
    return render(request, 'signup.html')

def Profile_view(request):
    return render(request, 'admin/profile.html')

# views.py
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Login_Staff')
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'admin/profile.html', {'user': request.user})
