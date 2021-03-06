from django.db import models
from django.db.models.fields.related import RelatedField
from django.conf import settings
import os


class AbstractTypeModel(models.Model):
    value = models.CharField(max_length=120)

    class Meta:
        abstract = True

    def __str__(self):
        return self.value

    @classmethod
    def load_initial(cls, values, pet_type):
        for value in values.split('\n'):
            cls.objects.get_or_create(value=value.strip().lower())


class TypeField(models.ForeignKey):
    pass


class PetType(AbstractTypeModel):
    pass


class EarType(AbstractTypeModel):
    pass


class TailType(AbstractTypeModel):
    pass


class PetTypeSensitiveAbstractTypeModel(AbstractTypeModel):
    pet_type = models.ForeignKey(PetType, on_delete=models.SET_NULL, null=True)

    @classmethod
    def load_initial(cls, values, pet_type):
        for value in values.split('\n'):
            cls.objects.get_or_create(value=value.strip().lower(), pet_type=pet_type)


class ColorType(PetTypeSensitiveAbstractTypeModel):
    pass


class FursType(PetTypeSensitiveAbstractTypeModel):
    pass


class Breed(PetTypeSensitiveAbstractTypeModel):
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


class SterilizationType(AbstractTypeModel):
    pass


class Pet(models.Model):
    accounting_card = models.CharField(max_length=128, unique=True, null=False)
    birthdate = models.DateField(null=False)
    weight = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    name = models.CharField(max_length=128, null=True)
    gender = TypeField(PetGender, on_delete=models.SET_NULL, null=True)
    pet_type = TypeField(PetType, on_delete=models.SET_NULL, null=True)
    breed = TypeField(Breed, on_delete=models.SET_NULL, null=True)
    color = TypeField(ColorType, on_delete=models.SET_NULL, null=True)
    furs_type = TypeField(FursType, on_delete=models.SET_NULL, null=True)
    ears_type = TypeField(EarType, on_delete=models.SET_NULL, null=True)
    tail_type = TypeField(TailType, on_delete=models.SET_NULL, null=True)
    size_type = TypeField(SizeType, on_delete=models.SET_NULL, null=True)
    special_parameters = models.CharField(max_length=128)
    aviary = models.CharField(max_length=10, null=True)

    # special info
    id_label = models.CharField(max_length=128)
    sterilization_status = TypeField(SterilizationType, on_delete=models.SET_NULL, null=True)
    sterilization_date = models.DateField(null=True)
    vet = models.ForeignKey('authentication.Vet', on_delete=models.SET_NULL, null=True)
    socialized = models.BooleanField(null=True)

    # catching
    work_order = models.CharField(max_length=32, null=True)
    work_order_date = models.DateField(null=True)
    administration_area = models.ForeignKey('manufacture.AdministrativeRegion', on_delete=models.SET_NULL, null=True)
    catching_act = models.CharField(max_length=32, null=True)
    catching_address = models.CharField(max_length=256, null=True)

    # new owners
    legal_entity = models.ForeignKey('manufacture.LegalEntity', on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey('authentication.PetOwner', on_delete=models.SET_NULL, null=True)

    # movement
    recipient_date = models.DateField(null=True)
    recipient_act = models.CharField(max_length=128, null=True)
    disposals_date = models.DateField(null=True)
    disposals_cause = TypeField(DisposeCause, on_delete=models.SET_NULL, null=True)
    death_cause = TypeField(DeathCause, on_delete=models.SET_NULL, null=True)
    euthanasia_cause = TypeField(EuthanasiaCause, on_delete=models.SET_NULL, null=True)
    contract_act = models.CharField(max_length=128, null=True)

    # Caregivers
    caregiver = models.ForeignKey('authentication.Caregiver', on_delete=models.SET_NULL, null=True)

    # shelter
    shelter = models.ForeignKey('manufacture.Shelter', on_delete=models.SET_NULL, null=True)

    # special
    description = models.CharField(max_length=128, null=True)

    # system
    create_time = models.DateTimeField(auto_created=True, auto_now_add=True, editable=False)
    last_update_time = models.DateTimeField(auto_now=True, editable=False)

    @classmethod
    def get_field_names(cls):
        return tuple(field.name for field in cls._meta.get_fields())

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
    number = models.CharField(max_length=50, null=True)
    date = models.DateField(null=True)
    product_name = models.CharField(max_length=128, null=True)
    dose = models.CharField(max_length=20, null=True)


class Vaccination(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='vaccination')
    number = models.CharField(max_length=50, null=True)
    date = models.DateField(null=True)
    vac_type = models.CharField(max_length=128, null=True)
    serial_number = models.CharField(max_length=50, null=True)


class HealthStatus(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='health_status')
    inspection_date = models.DateField(null=True)
    anamnesis = models.CharField(max_length=40, null=True)


class PetImage(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="static/img/")

    def absolute_url(self):
        return self.image.url
