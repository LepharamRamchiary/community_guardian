from django.shortcuts import render

def leanding(request):
    # return HttpResponse("Hello, world, Home")
    return render(request, 'leanding/leanding.html')

def about_us(request):
    return render(request, 'about-us/about_us.html')