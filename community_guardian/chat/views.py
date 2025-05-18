from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
from django.db.models import Q

@login_required
def chat(request, username=None):
    users = User.objects.exclude(id=request.user.id)
    # Fetch all messages for global chat
    messages = Message.objects.all().order_by('timestamp')

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            # For global chat, you can set receiver to None or skip the field if you make it nullable
            Message.objects.create(sender=request.user, content=content)
            return redirect('chat', username=request.user.username)

    return render(request, 'chat/chat.html', {
        'friend': None,
        'messages': messages,
        'users': users,
    })