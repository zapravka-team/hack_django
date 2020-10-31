from rest_framework import serializers as ser
from .models import Vet, Caregiver, PetOwner


class PetOwnerSerializer(ser.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = ['nlp']


class VetSerializer(ser.ModelSerializer):
    class Meta:
        model = Vet
        fields = ['nlp']


class CaregiverSerializer(ser.ModelSerializer):
    class Meta:
        model = Caregiver
        fields = ['nlp']
