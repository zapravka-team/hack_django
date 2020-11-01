from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_swagger.views import get_swagger_view
auto_schema = get_swagger_view(title='swagger')

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('pets/', include('pet.urls')),
                  path('report/', include('report.urls')),
                  path('manual/', include('manual.urls')),
                  path('swagger/', auto_schema),
                  path('api-auth/', include('rest_framework.urls')),
                  path('auth/', include('rest_auth.urls')),
                  path('auth/registration/', include('rest_auth.registration.urls'))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
