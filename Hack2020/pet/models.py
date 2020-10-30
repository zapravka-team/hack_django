from django.db import models

# Create your models here.

PET_TYPES = (
    ('dog', 'DOG'),
    ('cat', 'CAT')
)


class Pet(models.Model):
    accounting_card = models.CharField(max_length=20, unique=True, null=False)
    pet_type = models.CharField(max_length=40, null=False, choices=PET_TYPES)
    birthdate = models.DateField(null=False)
    weight = models.ImageField(null=False)
    name = models.CharField(max_length=128)
    gender
    bread
    color
    wool_type
    ears_type
    tail_type
    size_type
    special_parametrs
    avairy

    # special info
    id_label
    socilzed
    sterilized
    sterilization_date
    vet_nlp
    socialized

    # catching
    work_order
    administration_area
    catching_act
    catching_adres

    # owners
    ...

    # health
    inspection_date
    anamnesis


class Treatment(models.Model):
    pet
    number
    date
    product_name
    dose


class Vaccination(models.Model):
    pet
    number
    date
    vac_type
    seria_number
