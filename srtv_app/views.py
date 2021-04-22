from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import Show

# Create your views here.


def index(request):
    context={
        'shows':Show.objects.all()
    }
    return render(request,'shows.html',context)

def show_create(request):
    return render(request,'new_show.html')

def create_show(request):
    show=Show.objects.all()
    title=request.POST['title']
    network=request.POST['network']
    release_date=request.POST['release_date']
    description=request.POST['description']
    Show.objects.create(
        title=title,
        network=network,
        release_date=release_date,
        description=description,
    )
    print(request.POST)
    return redirect('/')

def edit(request,show_id):
    show=Show.objects.get(id=show_id)
    title=request.POST['title']
    network=request.POST['network']
    release_date=request.POST['release_date']
    descritption=request.POST['descritption']
    Show.objects.update(
        title=title,
        network=network,
        release_date=release_date,
        descritption=descritption
    )
    show.save()
    return redirect('/')

def view_show(request,show_id):
    show=Show.objects.get(id=show_id)
    context={
        'show':show
    }
    return render(request,'view_show.html',context)
    
    
def delete(request,show_id):
    show=Show.objects.get(id=show_id)
    show.delete()
    return redirect('/')

def edit_show(request,show_id):
    show=Show.objects.get(id=show_id)
    context={
        'show':Show.objects.all()
    }
    return render(request,'edit_show.html',context)

