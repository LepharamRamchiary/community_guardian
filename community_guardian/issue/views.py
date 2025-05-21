from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.db.models import Q
from .models import Issue, Comment
from .forms import IssueForm
from django.urls import reverse

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
            return redirect('my_issue')
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
    comments = issue.comments.filter(parent=None).order_by('-created_at')
    from_my_issues = request.GET.get('source') == 'my_issue'
    context = {
        'issue': issue,
        'comments': comments,
        'from_my_issues': from_my_issues,
        # Other context variables
    }
    return render(request, 'details_issue/details_issue.html', context)

@login_required
def edit_issue(request, issue_id):
    # Get the issue or return 404
    issue = get_object_or_404(Issue, id=issue_id)
    
    # Check if the current user is the owner of the issue
    if issue.user != request.user:
        return HttpResponseForbidden("You don't have permission to edit this issue.")
    
    if request.method == 'POST':
        form = IssueForm(request.POST, request.FILES, instance=issue)
        if form.is_valid():
            form.save()
            messages.success(request, "Issue updated successfully!")
            
            # Redirect to the issue detail page with source parameter
            # return redirect(f"{reverse('issue_detail', args=[issue_id])}?source=my_issue")
    else:
        form = IssueForm(instance=issue)
    
    return render(request, 'issue/edit_issue.html', {'form': form, 'issue': issue})

@login_required
def delete_issue(request, issue_id):
    # Get the issue or return 404
    issue = get_object_or_404(Issue, id=issue_id)
    
    # Check if the current user is the owner of the issue
    if issue.user != request.user:
        return HttpResponseForbidden("You don't have permission to delete this issue.")
    
    if request.method == 'POST':
        issue.delete()
        messages.success(request, "Issue deleted successfully!")
        return redirect('my_issue')
    
    return render(request, 'issue/delete_confirmation.html', {'issue': issue})


# comment
@login_required
def add_comment(request, issue_id):
    if request.method == 'POST':
        issue = get_object_or_404(Issue, id=issue_id)
        Comment.objects.create(
            issue=issue,
            user=request.user,
            text=request.POST['text']
        )
    return redirect(f"{reverse('issue_detail', kwargs={'issue_id': issue_id})}#comments")

@login_required
def add_reply(request, comment_id):
    if request.method == 'POST':
        parent = get_object_or_404(Comment, id=comment_id)
        Comment.objects.create(
            issue=parent.issue,
            user=request.user,
            text=request.POST['text'],
            parent=parent
        )
    return redirect(f"{reverse('issue_detail', kwargs={'issue_id': parent.issue.id})}#comments")

@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user in comment.likes.all():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)
    return redirect(f"{reverse('issue_detail', kwargs={'issue_id': comment.issue.id})}#comments")