from django.contrib import admin
from .models import Issue, Comment 

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'created_at')
    list_filter = ('status', 'category')
    search_fields = ('title', 'description')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('issue', 'user', 'text')
    filter_horizontal=('likes',)
