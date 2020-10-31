from rest_framework import serializers as ser

from .models import Shelter, OperatingOrganization, AdministrativeRegion


class OperationOrganizationSerializer(ser.ModelSerializer):
    class Meta:
        model = OperatingOrganization
        exclude = ['id']


class ShelterSerializer(ser.ModelSerializer):
    operating_organization = OperationOrganizationSerializer()

    class Meta:
        model = Shelter
        exclude = ['id']
