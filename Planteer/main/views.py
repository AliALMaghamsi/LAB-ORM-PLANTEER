from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from plants.models import Plant
from .models import Contact
# Create your views here.



def home_view(request:HttpRequest):

    return render(request,'main/index.html')

def contact_vew(request:HttpRequest):
    return render(request,'main/contact.html')

def error_view(request:HttpRequest):
    return render(request,'main/error.html')

def messages_view(request:HttpRequest):
    return render(request,'main/contact_messages.html')