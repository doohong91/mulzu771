from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, get_user_model


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
        return redirect('posts:list')
    else:
        form = UserCreationForm()        
        return render(request, 'accounts/signup.html', {'form': form})
    

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.user)
        return redirect('posts:list')
    else:
        form = AuthenticationForm(request)
        return render(request, 'accounts/login.html', {'form': form})
    

def logout(request):
    auth_logout(request)
    return redirect('posts:list')
    
    
def profile(request, username):
    profile = get_object_or_404(get_user_model(), username=username)
    return render(request, 'accounts/profile.html', {'profile': profile})