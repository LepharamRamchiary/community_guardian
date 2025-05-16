from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('report/', views.report_issue, name='report_issue'),  
    path('my_issue/', views.my_issue, name='my_issue'),  
    path('all_issues/', views.all_issues_public, name='all_issues_public'),
    path('details_issue/<int:issue_id>/', views.issue_detail, name='issue_detail'),
    path('edit_issue/<int:issue_id>/', views.edit_issue, name='edit_issue'),
    path('delete_issue/<int:issue_id>/', views.delete_issue, name='delete_issue'),

    #comment
    path('issue/<int:issue_id>/comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/reply/', views.add_reply, name='add_reply'),
    path('comment/<int:comment_id>/like/', views.like_comment, name='like_comment'),
]
