from django.db import models


class AdministrativeRegion(models.Model):
    name = models.CharField(max_length=128)


class OperatingOrganization(models.Model):
    name = models.CharField(max_length=128)

    @classmethod
    def load_data(cls, values):
        for value in values.split('\n'):
            cls.objects.get_or_create(name=value)


class Prefecture(models.Model):
    name = models.CharField(max_length=128)
    region = models.ForeignKey(AdministrativeRegion, on_delete=models.SET_NULL, null=True)
    operation_organization = models.ForeignKey(OperatingOrganization, on_delete=models.SET_NULL, null=True)


class Shelter(models.Model):
    address = models.CharField(max_length=256)
    name = models.CharField(max_length=128)
    operating_organization = models.ForeignKey(Prefecture, on_delete=models.SET_NULL, null=True)


class LegalEntity(models.Model):
    address = models.CharField(max_length=256, null=True)
    caregiver_list = models.CharField(max_length=256, null=True)
    phone_number = models.CharField(max_length=32, null=True)
