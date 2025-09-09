from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required 

# Homepage
def home(request):
    services=Service.objects.all()
    products=Product.objects.all()
    team_members=TeamMember.objects.all()
    abouts=About.objects.all()
    achievements=Achievement.objects.all()

    if request.method=="POST" and "contact_form" in request.POST:
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index.html")
    else:
        form=ContactForm()

    return render(request, "index.html",{"services":services,"products":products,"team_members":team_members,"abouts":abouts,"achievements":achievements,"form":form})

# Team Page
def team(request):
    founders=Founder.objects.all()
    core_team=CoreTeam.objects.all()
    tech_team=TechTeam.objects.all()
    return render(request, "team.html",{"founders":founders,"core_team":core_team,"tech_team":tech_team})

# Career Page
@login_required(login_url='auth')
def career(request):
    jobs=JobOpening.objects.all()
    if request.method=="POST" and "application_form" in request.POST:
        form=JobApplicationForm(request.POST)
        if form.isvalid():
            form.save()
            return redirect("career")
    else:
        form=JobApplicationForm()

    return render(request, "career.html",{"jobs":jobs,"form":form})

# Certifications Page
def certifications(request):
    certificates=Certification.objects.all()
    patents=Patent.objects.all()

    return render(request, "certifications.html",{"certificates":certificates,"patents":patents,})

# Notices Page
def notices(request):
    notices=Notice.objects.all()

    return render(request, "notice.html",{"notices":notices})

# Auth (Login + Register in one page)
def auth_view(request):
    if request.method == "POST" and "log_form" in request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # Try authentication
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect("home")  # change to your homepage
            else:
                messages.error(request, "Invalid credentials, please try again.")
    else:
        form = LoginForm()
    return render(request, "auth.html", {"form": form})

def register_view(request):
    # if request.method == "POST" and "register_form" in request.POST:
    #     form = RegisterForm(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.set_password(form.cleaned_data["password1"])  # hash password
    #         user.save()
    #         messages.success(request, "Account created successfully! Please login.")
    #         return redirect("auth")   # redirect to login page
    #     else:
    #         messages.error(request, "Please correct the errors below.")
    # else:
    #     form = RegisterForm()
    # return render(request, "register.html", {"form": form})
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        # Password check
        if pass1 != pass2:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        # Username will be full name (as per your request)
        username = name  

        # Check if username or email exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect("register")

        # Create user
        user = User.objects.create_user(username=username, email=email, password=pass1)
        user.first_name = name  # optional: store full name in first_name field
        user.save()

        messages.success(request, "Account created successfully! You can log in now.")
        return redirect("auth")

    return render(request, "register.html")





















def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("auth")