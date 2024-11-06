from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Plant


# Create your views here.


def all_plants_view(request:HttpRequest):
    return render(request,'plants/all_plants.html')

def new_plant_view(request:HttpRequest):
    return render(request,'plants/new_plant.html')

def plant_detail_view(request:HttpRequest,plant_id:int):
    return render(request,'plants/plant_detail.html')

def update_plant_view(request:HttpRequest,plant_id:int):
    return render(request,'plants/update_plant.html')

def delete_plant_view(request:HttpRequest,plant_id:int):
    return redirect('main:home_view')

def search_plant_view(request:HttpRequest):
    return render(request,'plants/search_plant_view.html')

