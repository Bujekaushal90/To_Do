from django.shortcuts import render
from ToDo.models import Task


def home(request):
    task = Task.objects.filter(is_completes = False)
    completed_task = Task.objects.filter(is_completes = True)
    context = {
        'task' : task,
        'completed_task' : completed_task
    }
    return render(request, 'home.html' , context)
    