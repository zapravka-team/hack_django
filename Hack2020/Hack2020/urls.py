from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('pets/', include('pet.urls')),
                  path('report/', include('report.urls')),
                  path('manual/', include('manual.urls')),
                  path('api-auth/', include('rest_framework.urls')),
                  path('auth/', include('rest_auth.urls')),
                  path('auth/registration/', include('rest_auth.registration.urls'))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
