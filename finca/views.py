from django.shortcuts import render
from tasks.models import task
from inventory.models import Cart
from tasks.forms import TaskForm
from inventory.forms import InventoryForm

def index(request):
    return render(request, "home.html")

def data(request):
    tasks = task.objects.all()
    carts = Cart.objects.all()
    tasks_missing = task.objects.filter(tcompletado=False)
    context = {'tasks': tasks, 'tasks_missing':tasks_missing, 'carts': carts, 'formT':TaskForm, 'formI':InventoryForm} 
    return render(request, "data.html", context=context)