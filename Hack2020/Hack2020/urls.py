from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pets/', include('pet.urls')),
    path('report/', include('report.urls')),
    path('manual/', include('manual.urls')),
    # path('auth/login,auth')auth
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls'))
]
