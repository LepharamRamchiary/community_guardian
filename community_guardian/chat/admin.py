from django.contrib import admin
from .models import Message 

@admin.register(Message)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('content', 'receiver', 'sender', 'timestamp')

