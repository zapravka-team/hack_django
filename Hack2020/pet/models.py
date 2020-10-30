from django.db import models


# Create your models here.

class AbstractTypeModel(models.Model):
    key = models.CharField(max_length=120)

    class Meta:
        abstract = True


class EarType(AbstractTypeModel):
    class Meta:
        abstract = False


class TailType(AbstractTypeModel):
    pass


class WoolType(AbstractTypeModel):
    pass


class Bread(AbstractTypeModel):
    pass


class PetType(AbstractTypeModel):
    pass


class ColorType(AbstractTypeModel):
    pass


class SizeType(AbstractTypeModel):
    pass


class AdministrationArea(AbstractTypeModel):
    pass


class PetOwner(models.Model):
    name = models.CharField(max_length=128)


# not in use
class Vet(models.Model):
    name = models.CharField(max_length=128)


class Pet(models.Model):
    accounting_card = models.CharField(max_length=128, unique=True, null=False)
    pet_type = models.ForeignKey(PetType, on_delete=models.SET_NULL, null=True)
    birthdate = models.DateField(null=False)
    weight = models.IntegerField(null=False)
    name = models.CharField(max_length=128)
    gender = models.SmallIntegerField(choices=((0, 'Male'), (1, 'Female')))
    bread = models.ForeignKey(Bread, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(ColorType, on_delete=models.SET_NULL, null=True)
    wool_type = models.ForeignKey(WoolType, on_delete=models.SET_NULL, null=True)
    ears_type = models.ForeignKey(EarType, on_delete=models.SET_NULL, null=True)
    tail_type = models.ForeignKey(TailType, on_delete=models.SET_NULL, null=True)
    size_type = models.ForeignKey(SizeType, on_delete=models.SET_NULL, null=True)
    special_parameters = models.CharField(max_length=128)
    aviary = models.IntegerField()

    # special info
    id_label = models.CharField(max_length=128)
    sterilized = models.BooleanField()
    sterilization_date = models.DateField(null=True)
    vet_nlp = models.CharField(max_length=128, null=True)
    socialized = models.BooleanField()

    # catching
    work_order = models.CharField(max_length=32)
    administration_area = models.ForeignKey(AdministrationArea, on_delete=models.SET_NULL, null=True)
    catching_act = models.CharField(max_length=32)
    catching_address = models.CharField(max_length=256)

    # owners
    owner = models.ForeignKey(PetOwner, on_delete=models.SET_NULL, null=True)

    # health
    inspection_date = models.DateField(null=False)
    anamnesis = models.CharField(max_length=40)


class Treatment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    date = models.DateField(null=False)
    product_name = models.CharField(max_length=128)
    dose = models.CharField(max_length=20)


class Vaccination(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    date = models.DateField(null=False)
    vac_type = models.CharField(max_length=128)
    seria_number = models.IntegerField()
