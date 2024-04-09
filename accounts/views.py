from .forms import MyUserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password

from django.views import View
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from.models import UserProfile
from .forms import *
from task_manager.models import Task
from blogs.models import Blog



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


       
    
class Logout(View):
    def get(self, request):
        logout(self.request)
        messages.success(request, 'Successfully logged out.')
        return redirect ( '/')
    

# @login_required

class Profile(View):
    def get(self, request, id):
        user = UserProfile.objects.get(id=id)
        form = EditProfileForm(instance=user)
        tasks = Task.objects.filter(assigned_to=user)[:5]
        blogs = Blog.objects.all()[:3]
        if self.request.user == user:
            password_form = ChangePasswordForm()
            title = 'My'
        else:
            password_form = ResetPasswordForm()
            title = 'User'
        return render(request, 'staff/profile.html', {'user_obj': user, 'tasks':tasks, 'blogs':blogs, 'form':form,'password_form':password_form, 'title':title })
    
    def post(self,request, id):
        user = UserProfile.objects.get(id=id)
        form = EditProfileForm(instance=user, data=self.request.POST, files=self.request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            form.save_m2m()
            messages.warning(self.request,'Profile updated successfully')
            return redirect( 'profile', id=id)
        else:
            messages.warning(self.request,'unable to update profile')
            
            return render(request, 'staff/profile.html', {'user_obj':user})



class ChangePassword(View):
    def post(self, request, id):
        user = UserProfile.objects.get(id=id)
        updating = False
        if self.request.user == user:
            password_form = ChangePasswordForm(data=self.request.POST)
            updating = True
        else:
            password_form = ResetPasswordForm(data=self.request.POST)

        if password_form.is_valid():
            if updating:
                if check_password(password_form.data['current_password'],user.password): 
                    if password_form.data['new_password'] == password_form.data['retype_new_password']: 
                        new_pw = password_form.data['new_password']
                        user.set_password(new_pw)
                        user.save()
                        messages.success(self.request,'successfully changed ur pw')
                        return redirect ('profile', id=id)
                
                else:
                    messages.warning(self.request,'new pw dont match')
                    return redirect ('profile', id=id)
            else:
                messages.warning(self.request,'old pw dont match')
                return redirect ('profile', id=id)
        else:
            messages.warning(self.request,'recheck ur input')
            # return redirect ('change_password', pk=user.id)
            return render(request, 'staff/profile.html',{'user':user, 'password_form':password_form})
    


# users
class UsersList(View):
    def get (self, *args, **kwargs):
        model = UserProfile
        if not model:
            messages.error(self.request, "Page not found!")
            return redirect("admin_dashboard")
        
        model, 
        objs = model.objects.all()
        list_fields = getattr(model, 'list_fields',[])
        return render(self.request, "staff/accounts/list_user.html",  {'objs':objs,'fields':list_fields}) 



class AddUser(View):
    def get(self,*args, **kwargs):
        return render(self.request, "staff/accounts/add_user.html", {'form':MyUserRegistrationForm()})
    def post(self, *args, **kwargs):
        form =  MyUserRegistrationForm(self.request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(self.request, "Successfully created user account")
            return redirect("users_list") 
    
        messages.error(self.request, "Invalid data detected!")
        return render(self.request, "staff/accounts/add_user.html", {'form':form})
    


class ResetPassword(View):

    def post(self, request, id):
        user = UserProfile.objects.get(id=id)
        password_form = ResetPasswordForm(data=self.request.POST)
        
        if password_form.is_valid():
            if password_form.data['new_password'] == password_form.data['retype_new_password']: 
                new_pw = password_form.data['new_password']
                user.set_password(new_pw)
                user.save()
                messages.success(self.request,'successfully changed user password')
                return redirect ('profile', id=id)
            
            else:
                messages.warning(self.request,'new password dont match')
                return redirect ('profile', id=id)
        else:
            messages.warning(self.request,'recheck ur input')
            # return redirect ('change_password', pk=user.id)
            return render(request, 'staff/profile.html',{'user_obj':user, 'password_form':password_form})
    


class DeleteUser(View):
    def get (self, request, id):
        user = UserProfile.objects.get(id=id)
        user.delete()
        return redirect ('users_list') 

