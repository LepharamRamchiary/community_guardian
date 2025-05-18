from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib import messages
import logging

# Set up logger
logger = logging.getLogger('django')

def register_view(request):
    try:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.save()
                messages.success(request, "Registration successful.")
                return redirect('login')  # Redirecting to login instead of refreshing the page
            else:
                # Log form validation errors
                logger.error(f"Form validation errors: {form.errors}")
        else:
            form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})
    except Exception as e:
        # Log any unexpected errors
        logger.error(f"Error in register_view: {str(e)}")
        messages.error(request, "An error occurred during registration. Please try again.")
        return render(request, 'accounts/register.html', {'form': RegisterForm()})

def login_view(request):
    try:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('leanding')
            else:
                # Log login errors
                logger.error(f"Login form errors: {form.errors}")
        else:
            form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})
    except Exception as e:
        # Log any unexpected errors
        logger.error(f"Error in login_view: {str(e)}")
        messages.error(request, "An error occurred during login. Please try again.")
        return render(request, 'accounts/login.html', {'form': AuthenticationForm()})

def logout_view(request):
    try:
        logout(request)
        return redirect('leanding')
    except Exception as e:
        # Log any unexpected errors
        logger.error(f"Error in logout_view: {str(e)}")
        return redirect('leanding')