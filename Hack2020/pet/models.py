from django.db import models


class AbstractTypeModel(models.Model):
    value = models.CharField(max_length=120)

    class Meta:
        abstract = True


class EarType(AbstractTypeModel):
    class Meta:
        abstract = False


class TailType(AbstractTypeModel):
    pass


class FursType(AbstractTypeModel):
    pass


class Bread(AbstractTypeModel):
    pass


class PetType(AbstractTypeModel):
    pass


class ColorType(AbstractTypeModel):
    pass


class SizeType(AbstractTypeModel):
    pass


class DisposeCause(AbstractTypeModel):
    pass


class DeathCause(AbstractTypeModel):
    pass


class EuthanasiaCause(AbstractTypeModel):
    pass


class PetGender(AbstractTypeModel):
    pass


class Pet(models.Model):
    accounting_card = models.CharField(max_length=128, unique=True, null=False)
    birthdate = models.DateField(null=False)
    weight = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    name = models.CharField(max_length=128)
    gender = models.ForeignKey(PetGender, on_delete=models.SET_NULL, null=True)
    pet_type = models.ForeignKey(PetType, on_delete=models.SET_NULL, null=True)
    bread = models.ForeignKey(Bread, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(ColorType, on_delete=models.SET_NULL, null=True)
    furs_type = models.ForeignKey(FursType, on_delete=models.SET_NULL, null=True)
    ears_type = models.ForeignKey(EarType, on_delete=models.SET_NULL, null=True)
    tail_type = models.ForeignKey(TailType, on_delete=models.SET_NULL, null=True)
    size_type = models.ForeignKey(SizeType, on_delete=models.SET_NULL, null=True)
    special_parameters = models.CharField(max_length=128)
    aviary = models.IntegerField()

    # special info
    id_label = models.CharField(max_length=128)
    sterilized = models.BooleanField()
    sterilization_date = models.DateField(null=True)
    vet = models.ForeignKey('authentication.Vet', on_delete=models.SET_NULL, null=True)
    socialized = models.BooleanField()

    # catching
    work_order = models.CharField(max_length=32)
    work_order_date = models.DateField()
    administration_area = models.ForeignKey('manufacture.AdministrativeRegion', on_delete=models.SET_NULL, null=True)
    catching_act = models.CharField(max_length=32)
    catching_address = models.CharField(max_length=256)

    # new owners
    owner = models.ForeignKey('authentication.PetOwner', on_delete=models.SET_NULL, null=True)

    # movement
    recipient_date = models.DateField()
    recipient_act = models.CharField(max_length=128)
    disposals_date = models.DateField()
    disposals_cause = models.ForeignKey(DisposeCause, on_delete=models.SET_NULL, null=True)
    death_cause = models.ForeignKey(DeathCause, on_delete=models.SET_NULL, null=True)
    euthanasia_cause = models.ForeignKey(EuthanasiaCause, on_delete=models.SET_NULL, null=True)
    contract_act = models.CharField(max_length=128)

    # Caregivers
    caregiver = models.ForeignKey('authentication.Caregiver', on_delete=models.SET_NULL, null=True)

    # shelter
    shelter = models.ForeignKey('manufacture.Shelter', on_delete=models.SET_NULL, null=True)

    # health
    ...

    # system
    create_time = models.DateTimeField(auto_created=True, auto_now_add=True, editable=False)
    last_update_time = models.DateTimeField(auto_now=True, editable=False)

    @classmethod
    def get_field_names(cls):
        return (field.name for field in cls._meta.get_fields())

    @classmethod
    def get_related_filed_names(cls):
        return


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
    serial_number = models.IntegerField()


class HealthStatus(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    inspection_date = models.DateField(null=False)
    anamnesis = models.CharField(max_length=40)
