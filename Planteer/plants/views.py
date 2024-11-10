from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Plant
from .forms import PlantForm
from django.core.paginator import Paginator

# Create your views here.


def all_plants_view(request:HttpRequest):
    page=request.GET.get('page')
    plants=Plant.objects.all()
    if "order_by" in request.GET and request.GET["order_by"]=="category":
        plants=plants.order_by("-category")
    elif "order_by" in request.GET and request.GET["order_by"]=="is_edible":
        plants=plants.order_by("-is_edible")

    paginator=Paginator(plants,4)
    page_obj=paginator.get_page(page)
    return render(request,'plants/all_plants.html',context={'plants':page_obj})

def new_plant_view(request:HttpRequest):
    plant_form=PlantForm()
    if request.method=='POST':
            plant_form=PlantForm(request.POST,request.FILES)
            if plant_form.is_valid():
                plant_form.save()
                return redirect('main:home_view')
            else:
                plant_form=PlantForm()

    return render(request,'plants/new_plant.html',context={'plant_form':plant_form , 'category':Plant.CategoryChoices.choices})

def plant_detail_view(request:HttpRequest,plant_id:int):
    try:
        plant=Plant.objects.get(pk=plant_id)
        print(plant.category)
    except Exception :
        return redirect('main:error_view')
    
    plants=Plant.objects.filter(category=plant.category).exclude(id=plant.id)[0:6]
    
    return render(request,'plants/plant_detail.html',context={'plant':plant,'plants':plants})

def update_plant_view(request:HttpRequest,plant_id:int):
    try:
        plant=Plant.objects.get(pk=plant_id)
        if request.method=='POST':
            plant=PlantForm(request.POST,request.FILES,instance=plant)
            if plant.is_valid():
                plant.save()
                return redirect('plants:all_plants_view')
            else:
                redirect('plants:update_plant_view',plant.id)
    except Exception :
        return redirect('main:error_view')
    
    return render(request,'plants/update_plant.html',context={'plant':plant,'category':Plant.CategoryChoices.choices})

def delete_plant_view(request:HttpRequest,plant_id:int):
    plant=Plant.objects.get(pk=plant_id)
    plant.delete()
    return redirect('main:home_view')

def search_plant_view(request:HttpRequest):

    if "search" in request.GET :
        plants= Plant.objects.filter(name__contains=request.GET["search"])
    else:
        plants=[]

    return render(request,'plants/search_plant.html',context={'plants':plants})

