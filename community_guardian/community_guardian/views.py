from django.shortcuts import render

def leanding(request):
    # return HttpResponse("Hello, world, Home")
    return render(request, 'leanding/leanding.html')