from rest_framework import serializers
from .models import contactUs
from django.db.models import fields

class contactUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = contactUs
        fields = '__all__'  
