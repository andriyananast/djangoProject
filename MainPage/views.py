from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'MainPage/MainPage.html')

def about(request):
    return render(request, 'MainPage/AboutPage.html')

def polls(request):
    return render(request, 'polls/pollspage.html')

# def seach(request):
#     return render(request, 'seach/seachresult.html')