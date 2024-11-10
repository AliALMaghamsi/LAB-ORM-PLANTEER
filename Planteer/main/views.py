from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from plants.models import Plant
from .models import Contact
from .forms import ContactForm
# Create your views here.



def home_view(request:HttpRequest):
    plants=Plant.objects.filter()[0:4]

    return render(request,'main/index.html',context={'plants':plants})

def contact_vew(request:HttpRequest):
    contact_form=ContactForm()
    if request.method =="POST":
        contact_form=ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect("main:home_view")
    return render(request,'main/contact.html')

def messages_view(request:HttpRequest):
    messages=Contact.objects.all()

    return render(request,'main/contact_messages.html',context={'messages':messages})

def error_view(request:HttpRequest):
    return render(request,'main/error.html')

