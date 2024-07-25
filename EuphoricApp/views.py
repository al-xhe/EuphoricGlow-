from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, FormContact
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def homePage(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def aboutPage(request):
    return render(request, 'about.html')

def productPage(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'detaliProduct.html', {'products': products})

def contactPage(request):
    if request.method == "POST":
        name = request.POST.get('firstName')
        surname = request.POST.get('lastName')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        if name and surname and email and comment:
            form_contact = FormContact(
                formContact_name=name,
                formContact_surname=surname,
                formContact_email=email,
                formContact_comment=comment
            )
            form_contact.save()
            messages.success(request, 'Message sent successfully!')
        else:
            messages.error(request, 'All fields are required.')
    return render(request, 'contact.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
       
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('registerPage')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('registerPage')

        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        messages.success(request, "Registration successful. Please log in.")
        return redirect('loginPage')
    
    return render(request, "auth/register.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('homePage')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('loginPage')
    
    return render(request, "auth/login.html")

def logout(request):
    auth_logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('homePage')

@login_required(login_url='loginPage')
def accessLogin(request):
    return render(request, "accessLogin.html")
