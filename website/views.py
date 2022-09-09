from django.shortcuts import render
def index(request):
    return render(request, 'website/base.html')

def courses(request):
    return render(request, 'website/courses.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')
