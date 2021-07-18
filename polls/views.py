from django.shortcuts import render
from .models import Task

# Create your views here.

def polls(request):
    tasks = Task.objects.all()
    return render(request, 'polls/pollspage.html', {'title': 'Мемесы', 'tasks': tasks})

def create(request):
    return render(request, 'polls/createpoll.html')