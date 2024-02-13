from .forms import MyUserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm



class Signup(View):
    def get(self,*args, **kwargs):
        return render(self.request, "register.html", {'form':MyUserRegistrationForm()})
    def post(self, *args, **kwargs):
        form =  MyUserRegistrationForm(self.request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(self.request, "Successfully created user account")
            return redirect("/") 
    
        messages.error(self.request, "Invalid data detected!")
        return render(self.request, "register.html", {'form':form})
    
    
class Login(View):
    def get (self, request):
        user = self.request.user
        if  user.is_authenticated:
            messages.info(self.request, "You are already logged in!")
            return redirect("/")
        return render (request, 'login.html', )
    
    def post (self, request):
        user = self.request.user
        email = request.POST.get('email')
        password = request.POST.get('password')
        form = AuthenticationForm(request)
        user = authenticate(request, username = email, password = password)
        
        if user is not None:
            if user.status == 'Active':
                login(request, user)        
                messages.success(request, f'Welcome back {user.first_name} {user.last_name}')
            elif user.status == 'Account Activation':
                messages.warning(request, f"Your account is being verified by our staff. Account status on {user.status}")    
            else:
                messages.warning(request, f"You can't login because your account status is on {user.status}.")    
                
            return redirect("/")
        

        else:
            print(form.errors)
            messages.warning(request, 'Email or password is wrong!',)
            return render(request, 'login.html', {'form':form})


        # return render(request, 'front/registration/login.html', {'form':AuthenticationForm})

    

class Logout(View):
    def get(self, request):
        logout(self.request)
        messages.success(request, 'Successfully logged out.')
        return redirect ( '/')
    

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
