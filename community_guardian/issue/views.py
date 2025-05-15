from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Issue
from .forms import IssueForm

# Create your views here.
@login_required
def report_issue(request):
    if request.method == 'POST':
        form = IssueForm(request.POST, request.FILES)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.user = request.user
            issue.save()
            messages.success(request, "Issue created successfully!")
            return redirect('report_issue')
    else:
        form = IssueForm()
    return render(request, 'issue/report_issue.html', {'form': form})

@login_required
def my_issue(request):
    issues = Issue.objects.filter(user=request.user).order_by('-created_at')
    paginator = Paginator(issues, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'issue/my_issues.html',  {'page_obj': page_obj})


@login_required
def all_issues_public(request):
    issues = Issue.objects.select_related('user').order_by('-created_at')
    paginator = Paginator(issues, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'issue/all_issues_public.html',  {'page_obj': page_obj})

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')