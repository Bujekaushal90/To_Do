from django.shortcuts import render
from ToDo.models import Task


def home(request):
    task = Task.objects.filter(is_completes = False)
    context = {
        'task' : task
    }
    return render(request, 'home.html' , context)
    