from django.contrib import admin

from .models import Pet, PetType, SizeType, FursType, TailType, EarType, ColorType, Vaccination, Treatment, Bread, \
    DisposeCause, EuthanasiaCause, PetGender, HealthStatus, DeathCause

# Register your models here.

admin.site.register(EarType)
admin.site.register(TailType)
admin.site.register(FursType)
admin.site.register(Bread)
admin.site.register(PetType)
admin.site.register(ColorType)
admin.site.register(SizeType)
admin.site.register(DisposeCause)
admin.site.register(EuthanasiaCause)
admin.site.register(PetGender)
admin.site.register(Pet)
admin.site.register(Treatment)
admin.site.register(Vaccination)
admin.site.register(HealthStatus)
admin.site.register(DeathCause)
