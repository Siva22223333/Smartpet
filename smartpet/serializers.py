from rest_framework import serializers
from .models import contactUs

class contactUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = contactUs
        fields = ['Name', 'Surname', 'Email', 'Message','Uploded_time'] 