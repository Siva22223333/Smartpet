from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('signin', views.signin, name='signin'),
    path('sell', views.sell, name='sell'),
    path('service', views.service, name='service'),
    path('contact', views.contact, name='contact'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('explore', views.explore, name='explore'),
    
]