from django.urls import path
from . import views

urlpatterns = [
    path('', views.smartpet, name='smartpet'),
]