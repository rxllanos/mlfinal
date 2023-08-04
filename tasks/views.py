from django.shortcuts import render, redirect
from .serializer import taskserializer
from .forms import TaskForm
from .models import task, Task_name
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages

@api_view(['GET'])
def apiOverview(request):
    api_urls ={
        'List':'/task-list/',
        'Detail':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = task.objects.all()
    serializer = taskserializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request,pk):
    task1 = task.objects.get(id=pk)
    
    serializer = taskserializer(task1,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def taskUpdate(request,pk):
    task1 = task.objects.get(id=pk)
    serializer = taskserializer(task1, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request,pk):
    task1 = task.objects.get(id=pk)
    task1.delete()
    return Response('item deleted')


def add(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Pendiente incluido!'))
            return redirect('data')
        else:
            messages.success(request, ('Try again!'))
            return redirect('data')