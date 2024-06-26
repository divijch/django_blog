from django.shortcuts import render, redirect
from . forms import RegistrationForm
from blogs.models import Blog
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def home(request):

    featured_posts = Blog.objects.filter(is_featured=True, status="Published").order_by('-created_at')
    posts = Blog.objects.filter(is_featured=False, status="Published").order_by('-created_at')
    context = {

        'featured_posts': featured_posts,
        'posts': posts
    }
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':   
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else: 
        form = RegistrationForm
    context = {
        'form': form,
    }
    
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')  # Use return to perform the redirection after login
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')