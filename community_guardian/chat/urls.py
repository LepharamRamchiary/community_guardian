from django.urls import path, include
from . import views

urlpatterns = [
     path('chat/<str:username>/', views.chat, name='chat'),
]