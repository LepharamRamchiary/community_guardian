from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ProfileEditForm
from django.contrib import messages
from issue.models import Issue
from django.http import JsonResponse

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

@login_required
def profile_view(request):
    # Example: Add additional context data
    # context = {
    #     'total_issues': 12,  # Replace with actual count from your models
    #     'resolved_issues': 8,
    #     'pending_issues': 4,
    #     'community_points': 25,
    # }
    user = request.user

    user_issues = Issue.objects.filter(user=user)   

    total_issues = user_issues.count()
    pending_issues = user_issues.filter(status='Pending').count()   
    resolved_issues = user_issues.filter(status='Resolved').count()
    processing_issues = user_issues.filter(status='Processing').count()
    rejected_issues = user_issues.filter(status='Rejected').count()

    community_points = (resolved_issues * 3) + (total_issues * 1)

    edit_form = ProfileEditForm(instance=user)

    context = {
        'total_issues': total_issues,
        'resolved_issues': resolved_issues,
        'pending_issues': pending_issues,
        'processing_issues': processing_issues,
        'rejected_issues': rejected_issues,
        'community_points': community_points,
        'edit_form': edit_form,
    }

    return render(request, 'profile/profile.html', context)



@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return JsonResponse({'success': True, 'message': 'Profile updated successfully!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'})