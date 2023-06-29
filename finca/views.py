from django.shortcuts import render
from tasks.models import task

def index(request):
    return render(request, "home.html")

def data(request):
    tasks = task.objects.all()
    tasks_missing = task.objects.filter(tcompletado=False)
    context = {'tasks': tasks, 'tasks_missing':tasks_missing } 
    return render(request, "data.html", context=context)