from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'website/index.html')
def about(request):
    return render(request, 'about/index.html')

def contact(request):
    return render(request, 'contact/index.html')