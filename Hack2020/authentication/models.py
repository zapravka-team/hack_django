from django.contrib.auth.models import AbstractUser
from django.db import models

from pet.models import Pet
from manufacture.models import OperatingOrganization, Prefecture, Shelter
from .managers import UserManager


class AdditionalPerson(models.Model):
    nlp = models.CharField(max_length=128)
    uuid = models.UUIDField(auto_created=True)

    class Meta:
        abstract = True


class PetOwner(AdditionalPerson):
    pass


class Vet(AdditionalPerson):
    pass


class Caregiver(AdditionalPerson):
    pass


DEPARTMENT_STAFF = 'DEPR'
OPERATION_ORGANIZATION_STAFF = 'OPER'
PREFECTURE_STAFF = 'PREF'
SHELTER_STAFF = 'SHTL'
COMMON_USER = 'USER'

ROLES = [
    (DEPARTMENT_STAFF, 'Сотрудник департамента'),
    (OPERATION_ORGANIZATION_STAFF, 'Сотрудник эксплоатирующей компнаии'),
    (PREFECTURE_STAFF, 'Сотрудник префектуры'),
    (SHELTER_STAFF, 'Сотрудник приюта'),
    (COMMON_USER, 'Пользователь'),
]


class SiteUser(AbstractUser):
    email = models.EmailField('email address', blank=True, unique=True)

    is_admin = models.BooleanField()
    role = models.CharField(max_length=4, choices=ROLES)

    last_name = None
    first_name = None

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class AdditionalUser(models.Model):
    user = models.OneToOneField(SiteUser, on_delete=models.SET_NULL, null=True)
    nlp = models.CharField(max_length=128)

    class Meta:
        abstract = True


class OperationOrganizationStaff(AdditionalUser):
    organization = models.ForeignKey(OperatingOrganization, on_delete=models.SET_NULL, null=True)


class ShelterStaff(AdditionalUser):
    shelter = models.ForeignKey(Shelter, on_delete=models.SET_NULL, null=True)


class PrefectureStaff(AdditionalUser):
    prefecture = models.ForeignKey(Prefecture, on_delete=models.SET_NULL, null=True)

