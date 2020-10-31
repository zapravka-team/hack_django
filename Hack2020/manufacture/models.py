from django.db import models


class AdministrativeRegion(models.Model):
    name = models.CharField(max_length=128)


class OperatingOrganization(models.Model):
    name = models.CharField(max_length=128)


class Prefecture(models.Model):
    name = models.CharField(max_length=128)
    region = models.ForeignKey(AdministrativeRegion, on_delete=models.SET_NULL, null=True)
    operation_organization = models.ForeignKey(OperatingOrganization, on_delete=models.SET_NULL, null=True)


class Shelter(models.Model):
    address = models.CharField(max_length=256)
    name = models.CharField(max_length=128)
    operating_organization = models.ForeignKey(Prefecture, on_delete=models.SET_NULL, null=True)
