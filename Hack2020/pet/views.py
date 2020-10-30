from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .serializer import PetSerializer
from .models import Pet
# Create your views here.

class PetView(ListAPIView):
    serializer_class = PetSerializer
    queryset = Pet.objects.all()
    fields = '__all__'
    class Meta:
        model = Pet
        fields = '__all__'
        fields = '__all__'