from django.contrib import admin

from .models import AdministrativeRegion, OperatingOrganization, Prefecture, Shelter

# Register your models here.
admin.site.register(Shelter)
admin.site.register(AdministrativeRegion)
admin.site.register(OperatingOrganization)
admin.site.register(Prefecture)