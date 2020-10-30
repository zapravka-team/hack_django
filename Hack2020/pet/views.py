from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from .serializer import PetSerializer
from .models import Pet


# Create your views here.

class PetView(ListCreateAPIView):
    serializer_class = PetSerializer
    queryset = Pet.objects.all()
