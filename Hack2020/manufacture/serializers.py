from rest_framework import serializers as ser

from .models import Shelter, OperatingOrganization, AdministrativeRegion, Prefecture


class OperationOrganizationSerializer(ser.Serializer):
    class Meta:
        model = OperatingOrganization
        exclude = ['id']


class ShelterSerializerLight(ser.ModelSerializer):
    operating_organization = ser.CharField(source='operating_organization.name')

    class Meta:
        model = Shelter
        exclude = ['id']


class ShelterSerializer(ser.ModelSerializer):
    operating_organization = OperationOrganizationSerializer()

    class Meta:
        model = Shelter
        exclude = ['id']


class AdministrativeRegionSerializer(ser.ModelSerializer):
    class Meta:
        model = AdministrativeRegion
        exclude = ['id']


class PrefectureSerializer(ser.ModelSerializer):
    class Meta:
        model = Prefecture
        exclude = ['id']
