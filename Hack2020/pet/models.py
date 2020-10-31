from django.db import models
from django.db.models.fields.related import RelatedField


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


class TypeField(models.ForeignKey):
    pass


class Pet(models.Model):
    accounting_card = models.CharField(max_length=128, unique=True, null=False)
    birthdate = models.DateField(null=False)
    weight = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    name = models.CharField(max_length=128)
    gender = TypeField(PetGender, on_delete=models.SET_NULL, null=True)
    pet_type = TypeField(PetType, on_delete=models.SET_NULL, null=True)
    bread = TypeField(Bread, on_delete=models.SET_NULL, null=True)
    color = TypeField(ColorType, on_delete=models.SET_NULL, null=True)
    furs_type = TypeField(FursType, on_delete=models.SET_NULL, null=True)
    ears_type = TypeField(EarType, on_delete=models.SET_NULL, null=True)
    tail_type = TypeField(TailType, on_delete=models.SET_NULL, null=True)
    size_type = TypeField(SizeType, on_delete=models.SET_NULL, null=True)
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
        return list(field.name for field in cls._meta.get_fields())

    @classmethod
    def get_related_filed_names(cls):
        related_fields = []
        for field in cls._meta.get_fields():
            if not isinstance(field, RelatedField):
                related_fields.append(field.name)
        return tuple(related_fields)

    @classmethod
    def get_type_filed_names(cls):
        related_fields = []
        for field in cls._meta.get_fields():
            if isinstance(field, RelatedField):
                if isinstance(field, TypeField):
                    related_fields.append(field.name)

        return tuple(related_fields)


class Treatment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='treatment')
    number = models.PositiveIntegerField()
    date = models.DateField(null=False)
    product_name = models.CharField(max_length=128)
    dose = models.CharField(max_length=20)


class Vaccination(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='vaccination')
    number = models.PositiveIntegerField()
    date = models.DateField(null=False)
    vac_type = models.CharField(max_length=128)
    serial_number = models.IntegerField()


class HealthStatus(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='health_status')
    inspection_date = models.DateField(null=False)
    anamnesis = models.CharField(max_length=40)
