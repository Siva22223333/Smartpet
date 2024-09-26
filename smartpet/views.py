from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import contactUs
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def login(request):
    template=loader.get_template('login.html')
    return HttpResponse(template.render())

def signin(request):
    template=loader.get_template('Signin.html')
    return HttpResponse(template.render()) 

def dashboard(request):
    template=loader.get_template('Dashboard.html')
    return HttpResponse(template.render())

def sell(request):
    template=loader.get_template('Sell.html')
    return HttpResponse(template.render())

def service(request):
    template=loader.get_template('service.html')
    return HttpResponse(template.render())

def contact(request):
    template=loader.get_template('contact.html')
    return HttpResponse(template.render())

def aboutus(request):
    template=loader.get_template('aboutus.html')
    return HttpResponse(template.render())

def explore(request):
    template=loader.get_template('explore.html')
    return HttpResponse(template.render())

def seemore(request):
    template=loader.get_template('seemore.html')
    return HttpResponse(template.render())


@api_view(['POST'])
def contactUS_POST(request):
    print("helllooooooooo")
    if request.method == 'POST':
        serializer = contactUsSerializers(data=request.data)
        if serializer.is_valid():
            Name=request.POST.get("name")
            Surname=request.POST.get("surname")
            Email=request.POST.get("email")
            Message=request.POST.get("message")
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
