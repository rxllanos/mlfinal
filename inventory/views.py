from django.shortcuts import render, redirect
from .serializer import Cart_nameserializer
from .models import Cart
from .forms import InventoryForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages

@api_view(['GET'])
def apiOverview1(request):
    api_urls ={
        'List':'/inventory-list/',
        'Detail':'/inventory-detail/<str:pk>/',
        'Create':'/inventory-create/',
        'Update':'/inventory-update/<str:pk>/',
        'Delete':'/inventory-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def inventoryList(request):
    carts = Cart.objects.all()
    serializer = Cart_nameserializer(carts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def inventoryDetail(request,pk):
    cart1 = Cart.objects.get(id=pk)
    serializer = Cart_nameserializer(cart1,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def inventoryUpdate(request,pk):
    cart1 = Cart.objects.get(id=pk)
    serializer = Cart_nameserializer(cart1, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def inventoryDelete(request,pk):
    cart1 = Cart.objects.get(id=pk)
    cart1.delete()
    return Response('inventory deleted')

def add(request):
    if request.method == "POST":
        form = InventoryForm(request.POST)
        if form.is_valid():
            inventory = form.cleaned_data["Cart"]
            inventory.save()
            messages.success(request, ('Item incluido!'))
            return redirect('data')
        else:
            messages.success(request, ('Try again!'))
            return redirect('data')
