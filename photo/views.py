from django.shortcuts import render, redirect
from .models import Category, Photo
from django.contrib.auth.decorators import login_required
# Create your views here.


def gallery(request):
    category = request.GET.get('category')
    categories = Category.objects.all()
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    context = {'categories': categories, 'photos': photos}  
    return render(request,'home.html', {'categories': categories, 'photos': photos})


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})


@login_required(login_url='employees:login')
def addPhoto(request):
    user = request.user
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                user=user,
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )
        return redirect('home')
    context = {'categories': categories}
    return render(request, 'photos/add.html', context)