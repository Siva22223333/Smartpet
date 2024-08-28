from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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