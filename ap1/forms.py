from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import ContactMessage,JobApplication
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



# class RegisterForm(forms.ModelForm):
#     # full_name=forms.CharField(label="Full Name",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Full Name'}))
#     # email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter email'}))
#     password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'placeholder':'Create Password'}))
#     password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
#     class Meta:
#         model=User
#         fields=["username","email","password1","password2"]

#     def clean_email(self):
#         email = self.cleaned_data.get("email")
#         if User.objects.filter(email=email).exists():
#             raise ValidationError("Email is already registered")
#         return email

#     def clean(self):
#         cleaned_data = super().clean()
#         password1 = cleaned_data.get("password1")
#         password2 = cleaned_data.get("password2")

#         if password1 and password2 and password1 != password2:
#             raise ValidationError("Passwords do not match")
#         return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Email or Username",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter email or username'
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
        })
    )

class ContactForm:
    class Meta:
        model=ContactMessage
        fields=["name","email","phone","message"]
        widgets={"name":forms.TextInput(attrs={"class":"form-control","placeholder":"Your Name"}),"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Your Email"}),"phone":forms.TextInput(attrs={"class":"form-control","placeholder":"Your Phone"}),"message":forms.Textarea(attrs={"class":"form-control","placeholder":"Your Message"})}

class JobApplicationForm:
    class Meta:
        model=ContactMessage
        fields=["job","name","email","message"]
        widgets={"job":forms.Select(attrs={"class":"form-select"}),"name":forms.TextInput(attrs={"class":"form-control","placeholder":"Your Name"}),"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Your Email"}),"message":forms.Textarea(attrs={"class":"form-control","placeholder":"Your Message"})}