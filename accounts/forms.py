# Create a file named forms.py in your app directory

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


# viewers registration
class MyUserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', 
            widget = forms.PasswordInput(attrs={'class': "form-control",'placeholder':'Password', 'autocomplete': "new-password",'placeholder': 'Password','minlength': 6,}))
    password2 = forms.CharField(label='Password confirmation',
            widget = forms.PasswordInput(attrs={'class':"form-control",'autocomplete':"new-password", 'placeholder':'Confirm password', 'minlength': 6,}))
    
    class Meta:
        model = UserProfile 
        fields = ['email', 'first_name','last_name','role', 'password', 'password2',  ]
        widgets = {
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email',}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name',}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name',}),
            'role':forms.Select(attrs={'class':'form-control', 'placeholder':'Select Role', 'type':'dropdown'}),
        }
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        # Save the provided password in hashed format
        myuser = super(MyUserRegistrationForm, self).save(commit=False)
        myuser.is_staff = True
        myuser.set_password(self.cleaned_data["password"])    
        if commit:
            myuser.save()
        return myuser
    