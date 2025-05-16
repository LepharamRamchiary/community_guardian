from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db.models import Q
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
    # Get filter parameters from request
    category = request.GET.get('category', '')
    status = request.GET.get('status', '')
    search = request.GET.get('search', '')
    
    # Start with all issues
    issues = Issue.objects.select_related('user').order_by('-created_at')
    
    # Apply filters if they exist
    if category:
        issues = issues.filter(category=category)
    
    if status:
        issues = issues.filter(status=status)
    
    if search:
        issues = issues.filter(Q(title__icontains=search))
    
    # Paginate the filtered results
    paginator = Paginator(issues, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Create context with page object and model choices
    context = {
        'page_obj': page_obj,
        'STATUS_CHOICES': Issue.STATUS_CHOICES,
        'CATEGORY_CHOICES': Issue.CATEGORY_CHOICES,
    }
    
    # Pass the context to the template
    return render(request, 'issue/all_issues_public.html', context)
    

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


@login_required
def issue_detail(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)
    from_my_issues = request.GET.get('source') == 'my_issue'
    context = {
        'issue': issue,
        'from_my_issues': from_my_issues,
        # Other context variables
    }
    return render(request, 'details_issue/details_issue.html', context)