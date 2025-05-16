from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('report/', views.report_issue, name='report_issue'),  
    path('my_issue/', views.my_issue, name='my_issue'),  
    path('all_issues/', views.all_issues_public, name='all_issues_public'),
    path('details_issue/<int:issue_id>/', views.issue_detail, name='issue_detail'),
]
