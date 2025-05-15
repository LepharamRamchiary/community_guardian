from django.db import models
from django.contrib.auth.models import User

class Issue(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Resolved', 'Resolved'),
        ('Rejected', 'Rejected')
    ]

    CATEGORY_CHOICES = [
        ('select_category', 'Select cateory'),
        ('road', 'Road Issue'),
        ('water', 'Water Issue'),
        ('electricity', 'Electricity Issue'),
        ('environment', 'Environment Issue'),
        ('other', 'Other'),
        
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='select_category')
    image = models.ImageField(upload_to='issue_images/')
    description = models.TextField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
